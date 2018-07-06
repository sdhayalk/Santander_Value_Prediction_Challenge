import numpy as np
import pandas as pd

from data_preprocessing import remove_constant_cols

train_df = pd.read_csv("../data/train.csv")
# test_df = pd.read_csv("../data/test.csv")

print("Train rows and columns : ", train_df.shape)
# print("Test rows and columns : ", test_df.shape)

remove_constant_cols(train_df)
# remove_constant_cols(test_df)

train_X = train_df.drop(["ID", "target"], axis=1)
# test_X = test_df.drop(["ID"], axis=1)
train_y = np.log1p(train_df["target"].values)   # Evaluation metric for the competition is RMSLE. Hence, using log of the target variable

