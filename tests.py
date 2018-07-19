from keras.models import load_model

import movie_dataset as movies


def main():
    saved_model_folder = 'saved_models/'
    model_name = 'genres_model2_tmp.h5'

    saved_model = load_model(saved_model_folder + model_name)
    x_test, y_test = movies.naver_load_genre_data('datas/images/Naver/test/')
    scores = saved_model.evaluate(x_test, y_test, verbose=0)
    print('Test loss: ', scores[0])
    print('Test accuracy: ', scores[1])


if __name__ == '__main__':
    main()