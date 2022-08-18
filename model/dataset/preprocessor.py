from __future__ import annotations
import librosa
import librosa.display
import numpy as np
import math


SAMPLING_RATE = 48000


def generate_spectrogram(problem: list[tuple[int, np.ndarray[np.float64]]], nsplit: int) -> np.ndarray[np.ndarray[np.float64]]:
    """スペクトログラムを生成する

    Args:
        problem (list[tuple[int, np.ndarray[np.float64]]]): 分割データ番号と分割データのタプルのリスト
        nsplit (int): 問題の分割数

    Returns:
        np.ndarray[np.ndarray[np.float64]]: スペクトログラム
    """

    audio_data = np.zeros(0)

    # 分割データがすべてそろっていない場合、
    # 与えられている分割データのサンプル数の平均をとり、 その平均が欠けている分割データのサンプル数であると考えて0でパディングする
    if len(problem) != nsplit:
        sample_sum = 0
        for i in range(len(problem)):
            sample_sum += len(problem[i][1])
        sample_avg = sample_sum / len(problem)

        exist_data_number = []
        lack_data_number = []
        for i in range(len(problem)):
            exist_data_number.append(problem[i][0])
        for i in range(1, nsplit + 1):
            if i not in exist_data_number:
                lack_data_number.append(i)

        for i in lack_data_number:
            problem.append((i, np.zeros(math.floor(sample_avg))))

    # タプルの1つめを基準にソートして分割データを結合
    problem.sort(key=lambda x: x[0])
    for _, split_data in problem:
        audio_data = np.concatenate([audio_data, split_data])

    # 短時間フーリエ変換を行い、スペクトログラムを作成
    # 短時間フーリエ変換の窓幅と移動幅を調整することにより、波形データの時間的な長さによらずスペクトログラムのサイズが一定となるようにする
    # 周波数軸:(1 + n_fft/2) × 時間軸:time_axis_length のサイズになるようにする
    time_axis_length = 2048  # 300 ~ 4000くらい 2000が中央くらい
    n_fft = 1024
    hop_length = math.floor(len(audio_data) / time_axis_length)

    D = librosa.stft(audio_data, n_fft=n_fft, hop_length=hop_length)
    strength = np.abs(D)
    strength_db = librosa.amplitude_to_db(strength, ref=np.max)

    if len(strength_db[0]) > time_axis_length:
        strength_db = np.delete(strength_db, slice(time_axis_length, None), 1)

    return strength_db


def preprocess(problem: list[tuple[int, np.ndarray[np.float64]]], nsplit: int) -> np.ndarray[np.ndarray[np.float64]]:
    """問題のデータからモデルへの入力を生成する

    Args:
        problem (list[tuple[int, np.ndarray[np.float64]]]): 分割データ番号と分割データのタプルのリスト
        nsplit (int): 問題の分割数

    Returns:
        np.ndarray[np.ndarray[np.float64]]: モデルへの入力とするスペクトログラム
    """

    spectrogram = generate_spectrogram(problem, nsplit)

    # 正規化
    spectrogram /= 80
    spectrogram += 1

    return spectrogram
