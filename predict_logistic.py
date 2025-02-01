import pickle



with open('trained_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

def predict(patient_info):
    return loaded_model.predict(patient_info)