import pandas as pd
import numpy as np

csv_file_path = 'datas/MovieGenre.csv'

def main():
    df = pd.read_csv(csv_file_path, encoding="ISO-8859-1")

    genres = df['Genre']
    result = np.zeros(24, dtype='int')
    i=0
    for tmp in genres:
        tmp = str(tmp).split('|', 5)
        for genre in tmp:
            if genre == 'Comedy':
                result[0] += 1
            elif genre == 'Drama':
                result[1] += 1
            elif genre == 'Action':
                result[2] += 1
            elif genre == 'Animation':
                result[3] += 1
            elif genre == 'Romance':
                result[4] += 1
            elif genre == 'Adventure':
                result[5] += 1
            elif genre == 'Horror':
                result[6] += 1
            elif genre == 'Sci-Fi':
                result[7] += 1
            elif genre == 'Crime':
                result[8] += 1
            elif genre == 'Mystery':
                result[9] += 1
            elif genre == 'Thriller':
                result[10] += 1
            elif genre == 'War':
                result[11] += 1
            elif genre == 'Family':
                result[12] += 1
            elif genre == 'Western':
                result[13] += 1
            elif genre == 'Documentary':
                result[14] += 1
            elif genre == 'Biography':
                result[15] += 1
            elif genre == 'Fantasy':
                result[16] += 1
            elif genre == 'Music':
                result[17] += 1
            elif genre == 'Sport':
                result[18] += 1
            elif genre == 'Musical':
                result[19] += 1
            elif genre == 'History':
                result[20] += 1
            elif genre == 'Short':
                result[21] += 1
            elif genre == 'Adult':
                print(df['Title'][i])
                result[22] += 1
            elif genre == 'Film-Noir':
                result[23] += 1
        i = i+1

    print(result)


if __name__ == "__main__":
    main()