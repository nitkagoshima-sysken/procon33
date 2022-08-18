from __future__ import annotations
import matplotlib.pyplot as plt


def learning_progress(model_name: str, train_loss: list[float], train_acc: list[float], val_loss: list[float], val_acc: list[float]) -> None:
    """学習曲線を保存する

    Args:
        model_name (str): モデルの名前
        train_loss (list[float]): 訓練データの損失
        train_acc (list[float]): 訓練データの正解率
        val_loss (list[float]): 検証データの損失
        val_acc (list[float]): 検証データの正解率
    """

    fig, ax = plt.subplots(nrows=2, ncols=1)
    ax[0].plot(range(1, len(train_loss) + 1), train_loss, label='train')
    ax[0].plot(range(1, len(val_loss) + 1), val_loss, label='valid')
    ax[0].legend()
    ax[0].set(title='loss')
    ax[0].set_xlabel('epoch')
    ax[0].set_ylabel('loss')

    ax[1].plot(range(1, len(train_acc) + 1), train_acc, label='train')
    ax[1].plot(range(1, len(val_acc) + 1), val_acc, label='valid')
    ax[1].set_ylim([0, 1])
    ax[1].legend()
    ax[1].set(title='accuracy')
    ax[1].set_xlabel('epoch')
    ax[1].set_ylabel('accuracy')

    fig.tight_layout()
    fig.savefig('./model/' + model_name + '_learning_progress.png')
