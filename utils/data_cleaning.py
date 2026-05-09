import pandas as pd

def show_unique(df: pd.DataFrame, columns: list[str], list:bool = False):
    for col in columns:
        unique_vals = df[col].unique()
        n_unique = df[col].nunique()
        print(f"Column: {col}")
        print(f"Unique count: {n_unique}")
        if list:
            sample_vals = list(unique_vals)
            print(f"Sample values: {sample_vals}")
