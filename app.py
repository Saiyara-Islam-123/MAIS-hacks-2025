from flask import Flask, render_template, request
import pandas as pd

#######################LOGIN STUFF

df_doctor_id_password = pd.read_excel("doctor_id_password.xlsx")
df_doctor_patient_info = pd.read_excel("doctor_id_patient_info.xlsx")

dict_doctor_id_password = df_doctor_id_password.set_index('doctor_id')['password'].to_dict()
doctor_to_patient_info = df_doctor_patient_info.set_index('doctor_id')['patient_info'].to_dict()

def login_check(doctor_id, password, ):
    if doctor_id not in dict_doctor_id_password:
        print(dict_doctor_id_password[doctor_id])
        print(dict_doctor_id_password[222])
        return False
    else:
        if password == dict_doctor_id_password[doctor_id]:
            return True
        else:
            return False

def create_new_user(doctor_id, password):
    if doctor_id not in dict_doctor_id_password:
        dict_doctor_id_password[doctor_id] = password
        doctor_to_patient_info[doctor_id] = []
        return "New user created"
    else:
        return "Current user, please log in"

def add_patient(doctor_id, patient_info):
    if doctor_id not in dict_doctor_id_password:
        doctor_to_patient_info[doctor_id].append(patient_info)

def update_excel():
    df_doctor_id_password = pd.DataFrame(dict_doctor_id_password)
    df_doctor_patient_info = pd.DataFrame(doctor_to_patient_info)

    df_doctor_id_password.to_excel("doctor_id_password.xlsx")
    df_doctor_patient_info.to_csv("doctor_id_patient_info.xlsx", index=False)


##############################################################Flask
app = Flask (__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        usr_name = request.form['username']
        usr_pwd = request.form['password']

        if 'login' in request.form:
            if login_check(usr_name, usr_pwd):
                return render_template('app.html')
            else:

                return render_template('login.html')


    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)