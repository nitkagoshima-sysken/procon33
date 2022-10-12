from __future__ import annotations
import numpy as np


def predict(problem: list[tuple[int, np.ndarray[np.float64]]], nsplit: int) -> list[int]:
    """いくつかの分割データから取る札を予測する

    Args:
        problem (list[tuple[int, np.ndarray[np.float64]]]): 分割データ番号と分割データのタプルのリスト
        nsplit (int): 問題の分割数

    Returns:
        list[int]: 取るべきと予測された札の番号
    """
    pass
