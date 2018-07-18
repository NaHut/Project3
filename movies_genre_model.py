import os
import time

import keras
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Dropout, Flatten
from keras.models import Sequential
from keras.models import Model, Input, Sequential
from keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D, Activation, Average, Dropout
from keras.utils import to_categorical
from keras.losses import categorical_crossentropy
from keras.callbacks import ModelCheckpoint, TensorBoard
from keras.optimizers import Adam
from keras.datasets import cifar10


def build(ratio, epochs,batch_size,
          x_train=None, y_train=None, x_validation=None, y_validation=None):

    print(' x_train shape: ', x_train.shape)
    print(x_train.shape[0], 'train samples')
    print(x_validation.shape[0], 'validation samples')

    #build model
    num_classes = len(y_train[0])


    model2 = Sequential([
        Conv2D(24, (5, 5), padding='same', input_shape=x_train.shape[1:], activation='relu'),
        Conv2D(24, (5, 5), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.25),

        Conv2D(48, (5, 5), padding='same', activation='relu'),
        Conv2D(48, (5, 5), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Dropout(0.25),

        Flatten(),
        Dense(256, activation='relu'),
        Dropout(0.5),
        Dense(num_classes, activation='sigmoid')

    ])

    model = Sequential([
        Conv2D(24, (3, 3), input_shape=x_train.shape[1:], activation='relu', padding='same'),
        Conv2D(24, (3, 3), activation='relu', padding='same'),
        Conv2D(24, (3, 3), activation='relu', padding='same'),
        MaxPooling2D(pool_size=(3, 3), strides=2),

        Conv2D(48, (3, 3), activation='relu', padding='same'),
        Conv2D(48, (3, 3), activation='relu', padding='same'),
        Conv2D(48, (3, 3), activation='relu', padding='same'),
        MaxPooling2D(pool_size=(3, 3), strides=2),

        Conv2D(48, (3, 3), activation='relu', padding='same'),
        Conv2D(48, (3, 3), activation='relu'),
        Conv2D(48, (3, 3)),

        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(num_classes, activation='sigmoid')
    ])




    # lr = 1e-4 -> 0.024
    opt = keras.optimizers.rmsprop(lr=1e-4, decay=1e-6)
    model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
    print(model.summary())

    # create save_dir
    save_dir = os.path.join(os.getcwd(), 'saved_models')
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)


    model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_data=(x_validation, y_validation))
    model_file_name = 'genres' + '_tmp.h5'

    model_path = os.path.join(save_dir, model_file_name)
    keras.callbacks.ModelCheckpoint(model_path,
                                    monitor='val_loss',
                                    verbose=0,
                                    save_best_only=False,
                                    save_weights_only=False,
                                    mode='auto',
                                    period=1)
    model.save(model_path)