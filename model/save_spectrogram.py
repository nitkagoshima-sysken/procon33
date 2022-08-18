from __future__ import annotations
import numpy as np
import matplotlib.pyplot as plt
import librosa

from model.dataset.preprocessor import generate_spectrogram


def save_spectrogram(problem: list[tuple[int, np.ndarray[np.float64]]], nsplit: int, save_path: str, spec_id: int) -> str:
    """スペクトログラムを生成して保存する

    Args:
        problem (list[tuple[int, np.ndarray[np.float64]]]): 分割データ番号と分割データのタプルのリスト
        nsplit (int): 問題の分割数
        save_path (str): スペクトログラムを保存するパス
        spec_id (int): _description_
    
    Returns:
        str: スペクトログラムのファイルへのパス
    """

    spectrogram = generate_spectrogram(problem, nsplit)

    # スペクトログラムを表示
    fig, ax = plt.subplots()
    img = librosa.display.specshow(
        spectrogram, sr=48000, x_axis='time', y_axis='log', ax=ax)
    ax.set(title='power spectrogram')
    fig.colorbar(img, ax=ax, format='%+2.f dB')
    file_path = save_path + 'spectrogram' + str(spec_id) + '.png'
    plt.savefig(file_path)

    return file_path
