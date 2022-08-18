import tensorflow as tf
from tensorflow import keras


def model_define() -> None:
    """モデルを定義して保存する
    """

    model = keras.models.Sequential()
    model.add(keras.layers.Conv2D(16, (5, 5), padding='same', activation='relu',
              input_shape=(513, 2048, 1)))
    model.add(keras.layers.MaxPooling2D((8, 8)))
    model.add(keras.layers.Conv2D(16, (5, 5), padding='same', activation='relu'))
    model.add(keras.layers.MaxPooling2D((8, 8)))
    model.add(keras.layers.Conv2D(16, (5, 5), padding='same', activation='relu'))

    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(128, activation='relu'))
    model.add(keras.layers.Dense(44, activation='sigmoid'))

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    # 他のモデルと名前が被らないようにする
    model_name = 'solver'
    model = model.save('./model/' + model_name)


if __name__ == '__main__':
    model_define()
