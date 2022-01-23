import pandas as pd
from get_screen import ScreenParser
import paths

def TableToImages(df_path, parser: ScreenParser):
    df = pd.read_csv(df_path)
    mails, urls = df['Email/Phone/Skype/UID'], df['URL/Почтовый ящик']

    for mail, url in zip(mails, urls):
        print(mail, url)
        parser.GetScreen(url, paths.SCREENSHOTS/f'{mail}.png')

if __name__ == '__main__':
    table_paths = [path
              for path in paths.PREPARED_DATA_PATH.iterdir()
              if path.suffix == '.xlsx']

    parser = ScreenParser()
    parser.SetUp()

    for path in table_paths:
        TableToImages(path, parser)