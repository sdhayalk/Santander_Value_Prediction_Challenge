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



train_df = pd.read_csv("../data/train.csv")
# test_df = pd.read_csv("../data/test.csv")

print("Train rows and columns : ", train_df.shape)
# print("Test rows and columns : ", test_df.shape)

remove_constant_cols(train_df)
# remove_constant_cols(test_df)
