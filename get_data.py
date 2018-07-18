import pandas as pd
import numpy as np
import urllib.request
from pathlib import Path

csv_file_path = 'datas/MovieGenre.csv'
poster_file_path = 'datas/images/100/'


def download(df):
    df_imdbId = df['imdbId']
    df_poster = df['Poster']
    i = 0

    for poster_url in df_poster:
        try:
            file_name = poster_file_path + str(df_imdbId[i]) + '.jpg'
            my_file = Path(file_name)
            if my_file.is_file():
                print('file already exist')
            else:
                urllib.request.urlretrieve(poster_url, file_name)
                print(file_name + 'downloaded')
        except:
            print('download error')
        i = i+1

def main():
    df = pd.read_csv(csv_file_path, encoding="ISO-8859-1")

    download(df)


if __name__ == "__main__":
    main()
