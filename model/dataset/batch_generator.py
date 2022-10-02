from __future__ import annotations
import numpy as np
import keras


class BatchGenerator(keras.utils.Sequence):
    """バッチデータのジェネレータ
    """

    def __init__(self, data_path: str, data_range_begin: int, data_range_end: int, batch_size: int = 64) -> None:
        self.data_num = (data_range_end - data_range_begin) + 1
        self.data_path = data_path
        self.data_range_begin = data_range_begin
        self.data_range_end = data_range_end
        self.batch_size = batch_size
        self.batches_per_epoch = int((self.data_num - 1) / self.batch_size) + 1


    def __getitem__(self, idx: int) -> tuple[np.ndarray[np.ndarray[np.ndarray[np.ndarray[np.float64]]]], np.ndarray[np.ndarray[np.float64]]]:
        """バッチ単位のデータとラベルを返す

        Args:
            idx (int): バッチのインデックス

        Returns:
            tuple[np.ndarray[np.ndarray[np.ndarray[np.ndarray[np.float64]]]], np.ndarray[np.ndarray[np.float64]]]:
            1バッチ分の前処理済みの問題と正答のタプル
        """

        batch_begin = self.data_range_begin + self.batch_size * idx
        batch_end = self.data_range_begin + self.batch_size * (idx + 1) - 1

        if batch_end > self.data_range_end:
            batch_end = self.data_range_end

        x_batch = []
        y_batch = []
        for i in range(batch_begin, batch_end + 1):
            data = np.load(self.data_path + 'data' + str(i) + '.npz')
            x_batch.append(np.reshape(data['image'], (513, 2048, 1)))
            y_batch.append(data['label'])

        x_batch = np.array(x_batch)
        y_batch = np.array(y_batch)

        return (x_batch, y_batch)


    def __len__(self) -> int:
        """1エポックのバッチサイズを返す

        Returns:
            int: 1エポックのバッチサイズ
        """
        return self.batches_per_epoch


    def on_epoch_end(self) -> None:
        """エポック終了時の処理
        """
        pass
