import numpy as np
import pandas as pd

def remove_constant_cols(df):
    unique_df = df.nunique().reset_index()
    unique_df.columns = ["col_name", "unique_count"]
    constant_df = unique_df[unique_df["unique_count"] == 1]

    for index, row in constant_df.iterrows():
        df.drop([row[0]], axis=1, inplace=True)

    # or simply, you can do:
    # df.drop(constant_df.col_name.tolist(), axis=1)

    return df


def main():
    pass

if __name__ == '__main__':
    main()