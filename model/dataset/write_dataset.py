import sys
sys.path.append('path_to_root_directory_of_this_project')
import numpy as np

from model.dataset.dataset import load
from model.dataset import preprocessor


def write_dataset() -> None:
    """データセットをストレージに書き込む
    """

    # ストレージの容量の許す量
    data_num = 110000

    # シードを固定して再現性をもたせる
    np.random.seed(0)

    for i in range(1, data_num + 1):
        problems, nsplits, correct_answers = load(data_num=1)

        image = np.array(
            preprocessor.preprocess(problems[0], nsplits[0]))
        label = np.array(correct_answers[0])

        # 各自の環境でパスを設定する必要がある
        np.savez('D:/procon33_dataset/data' + str(i),
                 image=image, label=label)


if __name__ == '__main__':
    write_dataset()
