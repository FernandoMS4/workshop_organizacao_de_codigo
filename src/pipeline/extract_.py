import glob as gl
import os
from typing import List

import pandas as pd

path = '../data/input'


def get_file_extract(path: str) -> List[pd.DataFrame]:
    all_files: str = gl.glob(os.path.join(path, '*.csv'))
    print(all_files)
    df_list: list = []
    for data in all_files:
        df_list.append(pd.read_csv(data))
    # df_final = pd.concat(df_list,ignore_index=True)
    return df_list


if __name__ == '__main__':
    df = get_file_extract(path)
    print(df)
