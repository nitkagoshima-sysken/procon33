from __future__ import annotations
import numpy as np
import librosa

from model.dataset.datatype import Information
from model.dataset.utility import to_file_name, to_speech_number, readdata_length


SAMPLING_RATE = 48000


def generate_problem_information() -> Information:
    """問題生成の必要な情報を生成する

    Returns:
        Information: 問題生成に必要な情報
    """

    information = Information()

    # 読みデータ数 3~20
    nspeech = np.random.randint(3, 21)

    # 読みデータ 英語版と日本語版の重複はない
    speech = []
    already_used_flag = [False] * 44
    for _ in range(nspeech):
        speech_number = np.random.randint(0, 88) + 1
        flag_index = speech_number
        if speech_number >= 45:
            flag_index -= 44
        while already_used_flag[flag_index - 1] == True:
            speech_number = np.random.randint(0, 88) + 1
            flag_index = speech_number
            if speech_number >= 45:
                flag_index -= 44
        already_used_flag[flag_index - 1] = True
        speech.append(to_file_name(speech_number, extension=True))

    # サンプル単位の開始位置
    offset = []
    offset_upperlimit = 50000
    for _ in range(nspeech):
        offset.append(np.random.randint(0, offset_upperlimit + 1))
    offset_min = min(offset)
    for i in range(nspeech):
        offset[i] -= offset_min

    # サンプル単位の冒頭の削除量
    begin = []
    begin_delete_upperlimit = 60000
    for _ in range(nspeech):
        begin.append(np.random.randint(0, begin_delete_upperlimit + 1))

    # サンプル単位の末尾の削除量
    end = []
    end_delete_upperlimit = 60000
    for _ in range(nspeech):
        end.append(np.random.randint(0, end_delete_upperlimit + 1))

    # 問題データのサンプル数を求める
    speech_length = []
    for i in range(nspeech):
        speech_length.append(readdata_length(to_speech_number(speech[i])))
    # 合成前の冒頭、末尾を削除した読みデータのサンプル数
    before_synthesize_length = [each_length - each_begin - each_end
                                for each_length, each_begin, each_end, in zip(speech_length, begin, end)]
    # 問題データのサンプル数
    problem_length = max([each_before_synthesize_length + each_offset
                          for each_before_synthesize_length, each_offset in zip(before_synthesize_length, offset)])

    # 分割数 2~5
    # サンプル単位の分割長の最小値 0.5秒分以上 * サンプリングレート48kHz
    split_data_minimam_length = int(0.5 * SAMPLING_RATE)
    splitable_max = problem_length / split_data_minimam_length
    split_max = min(5, splitable_max)
    nsplit = np.random.randint(2, split_max + 1)

    # サンプル単位の分割長 0.5秒分以上 * サンプリングレート48kHz -> 24000サンプル以上
    # 0.5秒分のデータを確保した後の、分配すべき余りのサンプル数
    excess_length = problem_length - (split_data_minimam_length * nsplit)
    devided_excess = []
    random_devided = []
    for _ in range(nsplit - 1):
        random_devided.append(np.random.randint(0, excess_length + 1))
    # 昇順にソート
    random_devided.sort()
    devided_excess.append(random_devided[0])
    for i in range(nsplit - 2):
        devided_excess.append(random_devided[i + 1] - random_devided[i])
    devided_excess.append(excess_length - random_devided[nsplit - 2])

    duration = [split_data_minimam_length +
                excess for excess in devided_excess]

    information.set_information(nspeech, speech, offset, begin, end,
                                before_synthesize_length, problem_length, nsplit, duration)

    return information


def generate_problem(information: Information) -> list[tuple[int, np.ndarray[np.float64]]]:
    """受け取った情報から、問題を生成する

    Args:
        information (Information): 問題を生成するのに必要な情報

    Returns:
        list[tuple[int, np.ndarray[np.float64]]]: 分割データの番号と分割データのタプルのリスト
    """

    synthesize_data = np.zeros(0)
    for i in range(information.nspeech):
        speech_data, sr = librosa.load(
            './model/dataset/src/' + information.speech[i], sr=SAMPLING_RATE)
        cut_data = speech_data[information.begin[i]: len(speech_data) - information.end[i]]
        shift_data = np.concatenate(
            [np.zeros(information.offset[i]), cut_data])
        if len(synthesize_data) < len(shift_data):
            synthesize_data = np.concatenate(
                [synthesize_data, np.zeros(len(shift_data) - len(synthesize_data))])
        elif len(synthesize_data) > len(shift_data):
            shift_data = np.concatenate(
                [shift_data, np.zeros(len(synthesize_data) - len(shift_data))])
        synthesize_data += shift_data

    # データを分割
    problem = []
    duration_base = 0
    for i in range(information.nsplit):
        problem.append(
            (i + 1, synthesize_data[duration_base: duration_base + information.duration[i]]))
        duration_base += information.duration[i]

    # 分割データをいくつか抜く
    remove_num = np.random.randint(0, information.nsplit)
    remove_indices = list(np.random.choice(
        range(0, information.nsplit), remove_num, replace=False))
    # 降順にソート
    remove_indices.sort(reverse=True)
    for i in remove_indices:
        del problem[i]

    return problem
