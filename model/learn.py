from __future__ import annotations
import tensorflow as tf

from dataset.batch_generator import BatchGenerator
from learning_progress import learning_progress


# バッチサイズ
# メモリが足りるなら32くらいが良い
BATCH_SIZE = 8


def learn(model: tf.keras.models.Model) -> tuple[tf.keras.models.Model, list[float], list[float], list[float], list[float]]:
    """モデルの学習を行う

    Args:
        model (tf.keras.models.Model): 学習を行うモデル

    Returns:
        tuple[tf.keras.models.Model, list[float], list[float], list[float], list[float]]:
        学習後のモデル、訓練データの損失、訓練データの正解率、検証データの損失、検証データの正解率
    """

    # 自らの環境でのデータセットへのパスを設定する必要がある
    train_generator = BatchGenerator(
        'D:/procon33_dataset/', 1, 100000, batch_size=BATCH_SIZE)
    val_generator = BatchGenerator(
        'D:/procon33_dataset/', 100001, 110000, batch_size=BATCH_SIZE)

    history = model.fit(
        train_generator,
        steps_per_epoch=train_generator.batches_per_epoch,
        validation_data=val_generator,
        validation_steps=val_generator.batches_per_epoch,
        epochs=100,
    )

    return (model, history.history['loss'], history.history['accuracy'], history.history['val_loss'], history.history['val_accuracy'])


def test(model: tf.keras.models.Model) -> tuple[float, float]:
    """モデルのテストを行う

    Args:
        model (tf.keras.models.Model): テストを行うモデル

    Returns:
        tuple[float, float]: テストデータの損失と正解率
    """

    test_generator = BatchGenerator(
        'D:/procon33_dataset/', 110001, 120000, batch_size=BATCH_SIZE)

    test_loss, test_acc = model.evaluate(
        test_generator,
        steps=test_generator.batches_per_epoch
    )

    return (test_loss, test_acc)


if __name__ == '__main__':
    with tf.device('/cpu:0'):

        model_name = 'solver'
        model_path = './model/' + model_name
        model = tf.keras.models.load_model(model_path)

        model, train_loss, train_acc, val_loss, val_acc = learn(model)
        print(train_loss, train_acc, val_loss, val_acc)

        model.save(model_path)

        learning_progress(model_name, train_loss, train_acc, val_loss, val_acc)

        test_loss, test_acc = test(model)
        print('test_loss:', test_loss)
        print('test_acc:', test_acc)
