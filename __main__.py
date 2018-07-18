import movie_dataset as movies
import movies_genre_model
import my_movies_genre_model


def main():

    train_path = 'datas/images/Naver/resize/'
    valiation_path = 'datas/images/Naver/validation/'
    print('train data loading')
    x_train, y_train = movies.naver_load_genre_data(train_path)
    # print('x_train shape : ', x_train.shape)
    #  print('y_train shape : ', y_train.shape)
    print('validation data loading')
    x_validation, y_validation = movies.naver_load_genre_data(valiation_path)
    # print('x_validation shape : ', x_validation.shape)
    # print('y_validation shape: ', y_validation.shape)
    ratio = 100
    epochs = 50
    batch_size = 4

    movies_genre_model.build(ratio, epochs, batch_size,
                            x_train=x_train,
                            y_train=y_train,
                            x_validation=x_validation,
                            y_validation=y_validation)

if __name__ == "__main__":
    main()