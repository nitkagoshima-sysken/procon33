from __future__ import annotations
import tensorflow as tf
import numpy as np

from model.dataset import preprocessor


def predict(model_name:str, problem: list[tuple[int, np.ndarray[np.float64]]], nsplit: int) -> list[int]:
    """いくつかの分割データから取る札を予測する

    Args:
        model_name (str): 予測に使うモデルの名前
        problem (list[tuple[int, np.ndarray[np.float64]]]): 分割データ番号と分割データのタプルのリスト
        nsplit (int): 問題の分割数

    Returns:
        list[int]: 取るべきと予測された札の番号
    """

    model = tf.keras.models.load_model('./model/' + model_name)

    spectrogram = np.array([preprocessor.preprocess(problem, nsplit)])

    model_output = model(np.reshape(spectrogram, (1, 513, 2048, 1)))

    speech = []
    speech_exist_border = 0.5
    for i, speech_exist_prob in enumerate(model_output[0]):
        if speech_exist_prob > speech_exist_border:
            speech.append(i + 1)

    return speech
