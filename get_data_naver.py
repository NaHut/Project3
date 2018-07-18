import pandas as pd
import numpy as np
import urllib.request
from pathlib import Path
import glob
from PIL import Image

csv_file_path = 'datas/MovieGenreFromNaver_2000.csv'
poster_file_path = 'datas/images/Naver/'


def download(df):
    df_poster = df['1']
    i = 0

    for poster_url in df_poster:
        try:
            file_name = poster_file_path + '100/'+ str(i) + '.jpg'
            my_file = Path(file_name)
            if my_file.is_file():
                print('file already exist')
            else:
                urllib.request.urlretrieve(poster_url, file_name)
                print(file_name + 'downloaded')
        except:
            print('download error')
        i = i+1

def resize():
    directory_path = poster_file_path + 'resize/'
    width = 202
    height = 290
    # image = Image.open(poster_file_path)

    path = poster_file_path + '100/' + '*.jpg'
    i = 0
    for file_name in glob.glob(path):
        image = Image.open(file_name)
        rgb_im = image.convert('RGB')
        re_image = rgb_im.resize((width, height))
        file_name = file_name.split('/', 5)
        file_name = file_name[4]
        re_image.save(directory_path + file_name)

def main():
    df = pd.read_csv(csv_file_path, encoding="UTF-8")

    # download(df)
    resize()

if __name__ == "__main__":
    main()
