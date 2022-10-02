from __future__ import annotations
import numpy as np


def to_file_name(speech_number: int, extension: bool = True) -> str:
    """読み札の番号をファイル名に変換する

    Args:
        speech_number (int):
        変換する読み札の番号 E01~E44 -> 1~44, J01~J44 -> 45~88
        extension (bool, optional): 拡張子を付けるか. Defaults to True.

    Returns:
        str: 指定された読み札のファイル名
    """

    speech_name = ''
    if 1 <= speech_number <= 44:
        speech_name += 'E'
    elif 45 <= speech_number <= 88:
        speech_name += 'J'
        speech_number -= 44

    speech_name += str(speech_number).zfill(2)
    if extension == True:
        speech_name += '.wav'

    return speech_name


def to_speech_number(file_name: str) -> int:
    """読み札のファイル名を番号に変換する

    Args:
        file_name (str): 変換する読み札のファイル名

    Returns:
        int: 指定された読み札の番号
    """

    speech_number = 0
    if file_name[0] == 'E':
        speech_number = int(file_name[1]) * 10 + int(file_name[2])
    elif file_name[0] == 'J':
        speech_number = int(file_name[1]) * 10 + int(file_name[2]) + 44

    return speech_number


def speech_encode(speech: list[str]) -> np.ndarray[np.float64]:
    """読み札のリストを0と1にエンコードする

    Args:
        speech (list[str]): 読み札のファイル名のリスト

    Returns:
        np.ndarray[np.float64]: 読み札のファイル名のリストにあるなら1、ないなら0とした取り札のリスト
    """

    vector = np.zeros(44)
    for speech_name in speech:
        vector[int(speech_name[1]) * 10 + int(speech_name[2]) - 1] = 1

    return vector


def readdata_length(speech_number: int) -> int:
    """読み札のファイルのサンプル数を返す

    Args:
        speech_number (int): 読み札の番号

    Returns:
        int: 指定された読み札のサンプル数
    """
    readdata_length = [
        269473,
        278344,
        226816,
        164596,
        249483,
        236321,
        279359,
        177870,
        257794,
        216279,
        247934,
        261813,
        285119,
        221142,
        235199,
        269744,
        175689,
        194583,
        167562,
        212862,
        264154,
        217845,
        303057,
        186507,
        213497,
        245170,
        241911,
        259470,
        219164,
        207986,
        218596,
        303260,
        239663,
        205273,
        205920,
        232310,
        248326,
        208317,
        257748,
        190126,
        237480,
        351356,
        224685,
        249599,
        350262,
        351762,
        349752,
        347044,
        394606,
        329004,
        336878,
        349169,
        324942,
        356009,
        323201,
        317325,
        330967,
        314939,
        347318,
        330663,
        333463,
        347120,
        321599,
        306073,
        319121,
        328991,
        331520,
        342490,
        316781,
        331230,
        318137,
        352895,
        341903,
        367059,
        317772,
        344916,
        318005,
        333757,
        330504,
        320074,
        332161,
        324119,
        314829,
        325214,
        326154,
        333808,
        307610,
        314342,
    ]

    return readdata_length[speech_number - 1]
