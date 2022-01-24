from pathlib import Path
import paths
import pandas as pd

from email_parser import models
from email_parser.get_screen import ScreenParser


def PrepareTable(xlsx_path: Path, parser: ScreenParser):
    df = pd.read_excel(xlsx_path)
    out = pd.DataFrame()
    out['url'] = df['URL/Почтовый ящик'].apply(lambda x: x.split(' ')[0])
    out['email'] = df['Email/Phone/Skype/UID'].apply(lambda x: x.split(' ')[0])
    out['image'] = parser.GetScreen(out['url'])

    return out

def AddToDB(df):
    objects = [item for item in zip(df.url, df.email, df.image)]
    models.FutureClient.objects.bulk_create(objects)

if __name__ == '__main__':
    parser = ScreenParser()
    parser.SetUp()


    paths = [xlsx for xlsx in paths.RAW_DATA_PATH.iterdir() if xlsx.suffix == '.xlsx']
    df = pd.concat([PrepareTable(item) for item in paths])
    AddToDB(df)

