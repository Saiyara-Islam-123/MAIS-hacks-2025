from flask import Flask, render_template, request, session
import pandas as pd
import os
from patient_funcs import *

#######################LOGIN STUFF



dict_doctor_id_password = {"benji" : "mew"}
doctor_to_patient_info = {"benji" : "no_file"}

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

    doctor_to_patient_info[doctor_id].append(patient_info)



def update_excel():
    list_id_password = []
    list_id_patient_info = []

    for key in dict_doctor_id_password:
        list_id_password.append(dict_doctor_id_password[key])
        list_id_patient_info.append(doctor_to_patient_info[key])

    column_1a = dict_doctor_id_password.keys()
    column_1b = list_id_password

    column_2a = doctor_to_patient_info.keys()
    column_2b = list_id_patient_info
    print(column_2a)
    print(column_2b)

    df_doctor_id_password = pd.DataFrame({'doctor_id': column_1a, 'password': column_1b})
    df_doctor_patient_info = pd.DataFrame({'doctor_id': column_2a, 'patient_info': column_2b})


    df_doctor_id_password.to_excel("doctor_id_password.xlsx")
    df_doctor_patient_info.to_excel("doctor_id_patient_info.xlsx")



##############################################################Flask
app = Flask (__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = "Saiyara"


@app.route("/")
def home():
    return render_template("login.html")

@app.route('/add_user', methods=['POST', 'GET'])
def add_user():
    if request.method == 'POST':
        usr_pwd = request.form['newpassword']
        usr_name = request.form['newusername']



        if ('signup' in request.form):

            if usr_name not in dict_doctor_id_password:

                create_new_user(usr_name, usr_pwd)
                update_excel()

                return render_template('profile.html')
            else:

                return render_template('login.html')

        return render_template("login.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        usr_name = request.form['username']
        usr_pwd = request.form['password']

        if 'login' in request.form:
            if login_check(usr_name, usr_pwd):
                session['username'] = usr_name

                return render_template('profile.html')
            else:

                return render_template('login.html')


    return render_template("login.html")

@app.route("/profile", methods=['POST', 'GET'])

def profile():
    if request.method == 'POST':
        if 'input' in request.form:
            return render_template('input_patient_info.html')

        else:
            return render_template("profile.html")
@app.route("/upload", methods=['POST', "GET"])
def upload():

    if request.method == 'POST':

        if 'username' in session:
            username = session['username']
            patient_info_file_name = doctor_to_patient_info[username]

        file = request.files['file']

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        ids, preds = analyze_file(file)

        if patient_info_file_name != "no_file":
            print("HELLLLLLO")
            files_list = patient_info_file_name.split[","]
            for i in range(len(files_list)):

                ids_2, preds_2 = analyze_file(files_list[i])

                ids = ids + ids_2
                preds = preds + preds_2


            doctor_to_patient_info[username] += "," + file.filename
            update_excel()

        else:
            #store the file; update excel

            doctor_to_patient_info[username] = "/uploads/" + file.filename
            print(doctor_to_patient_info[username])
            update_excel()

        return render_template("patient_dashboard.html", ids = ids, preds = preds)



if __name__ == '__main__':
    #update_excel()
    app.run(debug=True)