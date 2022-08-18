from __future__ import annotations
import numpy as np

from model.dataset.problem_generate import generate_problem_information, generate_problem
from model.dataset.utility import speech_encode


def load(data_num: int = 100) -> tuple[list[list[tuple[int, np.ndarray[np.float64]]]], list[int], list[np.ndarray[np.float64]]]:
    """問題を生成する

    Args:
        data_num (int, optional): 生成するデータ数. Defaults to 100.

    Returns:
        tuple[list[list[tuple[int, np.ndarray[np.float64]]]], list[int], list[np.ndarray[np.float64]]]:
        生成した問題のリスト、分割数のリスト、正解のリストのタプル
    """

    problems = []
    nsplits = []
    correct_answers = []

    for _ in range(data_num):
        information = generate_problem_information()
        problem = generate_problem(information)
        problems.append(problem)
        nsplits.append(information.nsplit)
        correct_answers.append(speech_encode(information.speech))

    return (problems, nsplits, correct_answers)
