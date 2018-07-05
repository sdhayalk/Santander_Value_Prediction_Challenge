import numpy as np
import pandas as pd

train_df = pd.read_csv("../data/train.csv")
test_df = pd.read_csv("../data/test.csv")

print("Train rows and columns : ", train_df.shape)
print("Test rows and columns : ", test_df.shape)

