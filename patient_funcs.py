import pandas as pd
from predict_logistic import *
import torch


def analyze_file(excel_file):
    df = pd.read_excel(excel_file)
    patient_ids = df["patient_id"]

    patient_info_pd = df.drop(columns = ["patient_id", "Unnamed: 1"])


    patient_info = torch.tensor(patient_info_pd.values, dtype=torch.float32)

    return patient_ids.tolist(), (predict(patient_info))

print(analyze_file("patients.xlsx"))