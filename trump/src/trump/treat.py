import pandas as pd

def describe_missing(df):
    missing = []

    for c in df.columns:
        count_missing = pd.isnull(df[c]).sum()
        if count_missing > 0:
            missing.append((c, round(count_missing / df.shape[0], 2)))

    return pd.DataFrame(missing, columns=['col', 'missings'])
