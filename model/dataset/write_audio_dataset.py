import sys
sys.path.append('path_to_root_directory_of_this_project')
import numpy as np
import soundfile

from model.dataset.dataset import load
from model.dataset.utility import concatenate_split_data


def write_dataset() -> None:
    """音声データのデータセットをストレージに書き込む
    """

    # ストレージの容量の許す量
    data_num = 10000

    # シードを固定して再現性をもたせる
    np.random.seed(0)

    for i in range(1, data_num + 1):
        problems, nsplits, correct_answers = load(data_num=1)
        audio = np.array(concatenate_split_data(problems[0], nsplits[0]))
        label = np.array(correct_answers[0])

        # 各自の環境でパスを設定する必要がある
        soundfile.write('any_path/data' + str(i) + '.wav', audio, 48000)
        np.save('any_path/label' + str(i) + '.npy', label)


if __name__ == '__main__':
    write_dataset()
