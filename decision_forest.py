import pandas as pd
import numpy as np
# from sklearn.model_selection import train_test_split

# Randomly sample 7 elements from your dataframe


def split_in_random(train_df_data, train_df_targets, N = 4):
    TOTAL = train_df_targets.shape[0]

    df = pd.concat([train_df_targets, train_df_data], axis=1)
    samples = []
    for i in range(N-1):
        sample = df.sample(int(TOTAL/N))
        df = df.loc[~df.index.isin(sample.index)]
        sample_target = sample.iloc[:, :1]
        sample_data = sample.iloc[:, 1:]
        samples.append((sample_target, sample_data))
    # last sample might be larger
    sample_target = df.iloc[:, :1]
    sample_data = df.iloc[:, 1:]
    samples.append((sample_target, sample_data))

    # print(samples)
    return samples















d1 ={0: [1, 2, 3, 4, 5, 6, 7, 8, 9],
     1: [1, 2, 3, 4, 5, 6, 7, 8, 9],
     2: [1, 2, 3, 4, 5, 6, 7, 8, 9],
     3: [1, 2, 3, 4, 5, 6, 7, 8, 9],
     4: [1, 2, 3, 4, 5, 6, 7, 8, 9]}

d2 ={0: [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]}

df1 = pd.DataFrame(data=d1)
df2 = pd.DataFrame(data=d2)

split_in_random(df1, df2)