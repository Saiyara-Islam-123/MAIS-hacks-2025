import pickle

with open('trained_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

dict_cat_to_severity = {0 : "None-minimal",
                        1: "Mild",
                        2: "Moderate",
                        3: "Moderately severe",
                        4: "Severe"
                        }

def predict(patient_info):
    return dict_cat_to_severity[loaded_model.predict(patient_info)], loaded_model.predict_proba(patient_info)
