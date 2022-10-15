from __future__ import annotations
import numpy as np
import librosa

from model.dataset.utility import to_file_name


def predict_by_sound_correlation(problem):
    # マッチングの開始位置のシフト量
    shift_width = 128
    # 48000Hzはサンプリングレートとして高いから、サンプル数を落としてもある程度は耐える
    # サンプリングレートを何分の1にするか
    skip_width = 32
    correlation_max_values = []
    for i in range(1, 89):
        read_data, sr = librosa.load('./model/dataset/src/' + to_file_name(i), sr=48000)
        section_correlation_max_values = []
        feature_sections = [read_data[i:i+24000] for i in range(5000, 120000, 24000)]
        for feature_section in feature_sections:
            correlations = []
            for matching_head in range(0, len(problem) - len(feature_section) + 1, shift_width):
                # 標準偏差を計算すると、小数点誤差により標準偏差が0となることがある
                # なので、100倍してから相関を求める
                # 双方のデータを定数倍して相関を計算しても、相関係数は変わらない
                # 高速化のために、行列じゃなくて相関係数だけを直接求める？
                # 差の絶対値の平均を計算すれば処理が軽くなる？
                correlation = np.corrcoef(problem[matching_head:matching_head + len(feature_section):skip_width]*100, feature_section[::skip_width]*100)[0][1]
                # 最大値だけ保持してればよくね？メモリ的にも
                correlations.append(correlation)
            section_correlation_max_values.append(np.max(correlations))
        correlation_max_values.append(np.max(section_correlation_max_values))

    id_corr_pair = []
    for i in range(1, 45):
        id_corr_pair.append((i, np.max([correlation_max_values[i - 1], correlation_max_values[i - 1 + 44]])))
    id_corr_pair.sort(key=lambda x: x[1], reverse=True)
    
    answer = []
    for id, corr in id_corr_pair:
        answer.append(id)

    return answer
