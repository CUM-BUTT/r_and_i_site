from pathlib import Path

import pandas as pd


def PrepareTable(df: pd.DataFrame):
    #df['Email/Phone/Skype/UID']
    df['URL/Почтовый ящик'] = df['URL/Почтовый ящик'].apply(lambda x: x.split(' ')[0])
    df['hash'] = df['URL/Почтовый ящик'].apply(lambda x: x.split(' ')[0])

    return df

if __name__ == '__main__':
    raw_data_path = Path('data/raw_xlsx')
    prepared_data_path = Path('data/ready_csv')

    paths = [xlsx for xlsx in raw_data_path.iterdir() if xlsx.suffix == '.xlsx']
    dfs = [pd.read_excel(item) for item in paths]
    dfs = [PrepareTable(df) for df in dfs]
    [df.to_csv(prepared_data_path/path.name) for df, path in zip(dfs, paths)]

