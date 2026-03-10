import pandas as pd
import os


def load_csv(path):

    if not os.path.exists(path):
        print("File not found.")
        return None

    try:
        df = pd.read_csv(path)

        print("\nDataset Loaded")
        print(f"Rows: {df.shape[0]}")
        print(f"Columns: {df.shape[1]}")

        return df

    except Exception as e:
        print("Error loading dataset:", e)
        return None


def preview_dataset(df):

    if df is None:
        print("No dataset loaded.")
        return

    print("\nDataset Preview")
    print(df.head())


def dataset_summary(df):

    if df is None:
        print("No dataset loaded.")
        return

    print("\nSummary")
    print(df.describe())


def detect_columns(df):

    numeric = df.select_dtypes(include="number").columns.tolist()
    categorical = df.select_dtypes(include="object").columns.tolist()

    print("\nNumeric columns:", numeric)
    print("Categorical columns:", categorical)

    return numeric, categorical


def detect_missing(df):

    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if len(missing) == 0:
        print("\nNo missing values.")
    else:
        print("\nMissing values:")
        print(missing)
