import pandas as pd


def generate_profile(df):

    profile = {}

    # Basic info
    profile["rows"] = df.shape[0]
    profile["columns"] = df.shape[1]

    # Column names
    profile["column_names"] = list(df.columns)

    # Data types
    profile["dtypes"] = df.dtypes.astype(str).to_dict()

    # Null counts
    profile["null_counts"] = df.isnull().sum().to_dict()

    # Null percentages
    profile["null_percentages"] = (
        (df.isnull().sum() / len(df)) * 100
    ).round(2).to_dict()

    # Duplicate rows
    profile["duplicate_rows"] = int(df.duplicated().sum())

    # Unique counts
    profile["unique_counts"] = df.nunique().to_dict()

    return profile