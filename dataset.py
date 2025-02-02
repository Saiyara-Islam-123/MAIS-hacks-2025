#higher score = higher category = more depressed
import pandas as pd
from sklearn.model_selection import train_test_split
import torch

def get_age(x):
    return 2025 - x

df_primary = pd.read_parquet("anon_processed_df_parquet.parquet")

df_secondary = df_primary.drop(columns=['race_white', 'race_black', "race_asian", "race_other", "phq9_score_end", "phq9_cat_start"])


df_cleaned = df_secondary.dropna().reset_index(drop=True)
df_cleaned["age"] = df_cleaned['birthyear'].apply(get_age)
df_cleaned = df_cleaned.astype('float64')

train_df, test_df = train_test_split(df_cleaned, test_size=0.2, random_state=4)

X_train = train_df.drop(columns=["phq9_cat_end"])
y_train = train_df[["phq9_cat_end"]].copy()

X_test = test_df.drop(columns=["phq9_cat_end"])
y_test = test_df[["phq9_cat_end"]].copy()


def get_test_train():
    return torch.tensor(X_train.values, dtype=torch.float32), torch.tensor(y_train.values, dtype=torch.float32), torch.tensor(X_test.values, dtype=torch.float32), torch.tensor(y_test.values, dtype=torch.float32)

X_test.iloc[[0, 1]].to_excel("patients.xlsx")