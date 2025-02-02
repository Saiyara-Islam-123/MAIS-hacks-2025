import pickle

with open('trained_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

dict_cat_to_severity = {0 : "None-minimal",
                        1: "Mild",
                        2: "Moderate",
                        3: "Moderately severe",
                        4: "Severe"
                        }
def cat_to_severity(cats):
    list_severity = []
    for cat in cats:
        list_severity.append(dict_cat_to_severity[cat])

    return list_severity


def predict(patient_info):
    preds = loaded_model.predict(patient_info)
    return cat_to_severity(preds)
