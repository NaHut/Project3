from keras.models import load_model
import pandas as pd
import movie_dataset as movies
import sys
import numpy as np
from PIL import Image
from scipy.stats import rankdata


base_address = 'datas/images/Naver/test/'
file_name = sys.argv[1]


def load_data(path):
    df = pd.read_csv('datas/MovieGenreFromNaver_2000.csv', encoding="UTF-8")

    im = Image.open(path)
    rgb_im = im.convert('RGB')
    x = np.array(rgb_im, dtype='float32')
    x = np.expand_dims(x, axis=0)

    index = movies.naver_get_index(path, df)
    if index == -1:
        print('index error')
    y = movies.naver_get_label(df['2'][index])

    return x, y


def print_result(result):
    print('result : ', result)
    result = np.array(result)
    rank = rankdata(result)
    print('rank : ', rank)

    first = np.where(rank == 6)[0][0]
    second = np.where(rank == 5)[0][0]
    third = np.where(rank == 4)[0][0]

    first_genre = convert_to_genre(first)
    second_genre = convert_to_genre(second)
    third_genre = convert_to_genre(third)

    first_prob = result[0][first]
    first_prob = str(int(first_prob*100)) + '%'
    second_prob = result[0][second]
    second_prob = str(int(second_prob*100)) + '%'
    third_prob = result[0][third]
    third_prob = str(int(third_prob*100)) + '%'
    print(first_genre, ':', first_prob, ", ",
          second_genre, ':', second_prob, ", ",
          third_genre, ':', third_prob)

def convert_to_genre(index):
    result = 'ERROR'
    if index == 0:
        result = 'Fanstasy'
    elif index == 1:
        result = 'Romance'
    elif index == 2:
        result = 'Crime'
    elif index == 3:
        result = 'Comedy'
    elif index == 4:
        result = 'Animation'
    elif index == 5:
        result = 'Action'

    return result


def main():
    saved_model_folder = 'saved_models/'
    model_name = 'genres_model2_tmp.h5'

    saved_model = load_model(saved_model_folder + model_name)
    x_test, y_test = load_data(base_address + file_name)
    print_result(saved_model.predict(x_test))
    # scores = saved_model.evaluate(x_test, y_test, verbose=0)
    # print('Test loss: ', scores[0])
    # print('Test accuracy: ', scores[1])


if __name__ == '__main__':
    main()