import numpy as np
import pandas as pd
import glob
from PIL import Image

label_num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def load_genre_data(path):
    image_list = []
    label_list = []

    df = pd.read_csv('datas/MovieGenre.csv',  encoding="ISO-8859-1")

    path = path + '*.jpg'
    i = 0
    for file_name in glob.glob(path):
        if i % 100 == 0:
            print(i, 'th loading')
        i = i + 1
        im = Image.open(file_name)
        rgb_im = im.convert('RGB')
        xs = np.array(rgb_im, dtype='float32')
        image_list.append(xs)

        index = get_index(file_name, df)
        if index == -1:
            print('index error')

        ys = get_label(df['Genre'][index])
        label_list.append(ys)

    image_list = np.array(image_list, dtype='float32')
    label_list = np.array(label_list, dtype='float32')
    # print(label_list.shape)
    # print(image_list.shape)
    return image_list, label_list


def naver_load_genre_data(path):
    image_list = []
    label_list = []


    df = pd.read_csv('datas/MovieGenreFromNaver.csv', encoding="UTF-8")

    path = path + '*.jpg'
    i =0
    for file_name in glob.glob(path):
        if i % 100 == 0:
            print(i, 'th loading')
        i = i + 1
        im = Image.open(file_name)
        rgb_im = im.convert('RGB')
        xs = np.array(rgb_im, dtype='float32')
        image_list.append(xs)

        index = naver_get_index(file_name, df)
        if index == -1:
            print('index error')
        ys = naver_get_label(df['2'][index])
        # print(ys)
        label_list.append(ys)

    image_list = np.array(image_list, dtype='float32')
    label_list = np.array(label_list, dtype='float32')
    # print(label_list.shape)
    # print(image_list.shape)
    print(label_num)
    for i in range(15):
        label_num[i] = 0



    return image_list, label_list


def get_label(genres):
    result = np.zeros(15)
    genres = str(genres).split('|', 5)

    for genre in genres:
        if genre == 'Comedy':
            result[0] = 1
        elif genre == 'Action':
            result[1] = 1
        elif genre == 'Animation':
            result[2] = 1
        elif genre == 'Romance':
            result[3] = 1
        elif genre == 'Adventure':
            result[4] = 1
        elif genre == 'Horror':
            result[5] = 1
        elif genre == 'Sci-Fi':
            result[6] = 1
        elif genre == 'Crime':
            result[7] = 1
        elif genre == 'Thriller':
            result[8] = 1
        elif genre == 'Documentary':
            result[9] = 1
        elif genre == 'Sport':
            result[10] = 1
        elif genre == 'Adult':
            result[11] = 1
        elif genre == 'Mystery':
            result[12] = 1
        elif genre == 'Drama':
            result[13] = 1
        elif genre == 'Fantasy':
            result[14] = 1

    return result


def naver_get_label(genres):
    result = np.zeros(15)
    genres = genres.split('[', 1)
    genres = genres[1].split(']', 1)
    genres = genres[0].split(' ', 6)
    for genre in genres:
        item = genre.split('\'', 2)

        if item[1] == 'Comedy':
            result[0] = 1
            label_num[0] += 1;
        elif item[1] == 'Action':
            result[1] = 1
            label_num[1] += 1;
        elif item[1] == 'Animation':
            result[2] = 1
            label_num[2] += 1;
        elif item[1] == 'Romance':
            result[3] = 1
            label_num[3] += 1;
        elif item[1] == 'Adventure':
            result[4] = 1
            label_num[4] += 1;
        elif item[1] == 'Horror':
            result[5] = 1
            label_num[5] += 1;
        elif item[1] == 'SF':
            result[6] = 1
            label_num[6] += 1;
        elif item[1] == 'Crime':
            result[7] = 1
            label_num[7] += 1;
        elif item[1] == 'Thriller':
            result[8] = 1
            label_num[8] += 1;
        elif item[1] == 'Documentary':
            result[9] = 1
            label_num[9] += 1;
        elif item[1] == 'War':
            result[10] = 1
            label_num[10] += 1;
        elif item[1] == 'Family':
            result[11] = 1
            label_num[11] += 1;
        elif item[1] == 'Mystery':
            result[12] = 1
            label_num[12] += 1;
        elif item[1] == 'Drama':
            result[13] = 1
            label_num[13] += 1;
        elif item[1] == 'Fantasy':
            result[14] = 1
            label_num[14] += 1;
        # else:
            # print(item[1])
    return result


def get_index(file_name, df):

    file_name = file_name.split("/", 3)
    file_name = file_name[3]
    file_name = file_name.split(".", 1)
    file_name = file_name[0]
    i = 0
    for imdbId in df['imdbId']:
        if str(imdbId) == file_name:
            return i
        else:
            i = i+1
    return -1


def naver_get_index(file_name, df):
    file_name = file_name.split("/", 4)
    file_name = file_name[4]
    file_name = file_name.split(".", 1)
    file_name = file_name[0]
    return int(file_name)


def main():
    load_genre_data()


if __name__ == "__main__":
    main()