from __future__ import annotations
import numpy as np

from model.correlation.sound_correlation import predict_by_sound_correlation


def predict(model_name:str, problem: list[tuple[int, np.ndarray[np.float64]]], nsplit: int) -> list[int]:
    """いくつかの分割データから取る札を予測する

    Args:
        model_name (str): 予測に使うモデルの名前
        problem (list[tuple[int, np.ndarray[np.float64]]]): 分割データ番号と分割データのタプルのリスト
        nsplit (int): 問題の分割数

    Returns:
        list[int]: 取るべきと予測された札の番号
    """
    audio_data = np.zeros(0)
    # タプルの1つめを基準にソートして分割データを結合
    problem.sort(key=lambda x: x[0])
    for _, split_data in problem:
        audio_data = np.concatenate([audio_data, split_data])
    
    answer = predict_by_sound_correlation(audio_data)

    return answer
