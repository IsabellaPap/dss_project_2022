from flask import Flask, request, render_template,url_for, redirect
import csv
import uuid
from datetime import date, datetime
from cv19index import predict
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'df0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25506'

@app.route("/form", methods=['GET','POST'])
  
def get_data():
  dx_list = []
  if request.method == 'POST':
    age = request.form['age']
    gender = request.form['gender']
    dx1 = request.form.get('dx1')
    if dx1:
      dx_list.append(dx1)
    dx2 = request.form.get('dx2')
    if dx2:
      dx_list.append(dx2)
    dx3 = request.form.get('dx3')
    if dx3:
      dx_list.append(dx3)
    dx4 = request.form.get('dx4')
    if dx4:
      dx_list.append(dx4)
    dx5 = request.form.get('dx5')
    if dx5:
      dx_list.append(dx5)
    dx6 = request.form.get('dx6')
    if dx6:
      dx_list.append(dx6)
    dx7 = request.form.get('dx7')
    if dx7:
      dx_list.append(dx7)
    dx8 = request.form.get('dx8')
    if dx8:
      dx_list.append(dx8)
    dx9 = request.form.get('dx9')
    if dx9:
      dx_list.append(dx9)
    dx10 = request.form.get('dx10')
    if dx10:
      dx_list.append(dx10)
    return redirect(url_for('data_prep',age = age, gender = gender, dx = dx_list))
  return render_template('input_form.html')

@app.route("/prep/<age>/<gender>/<dx>")

def data_prep(age,gender,dx):

  personid = str(uuid.uuid4())
  personid = personid.replace('-', '')
  personid = personid[0:16]
  
  # prep data for csv input
  data_demographics = [personid, age, gender]

  with open('demographics.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["personId","gender","age"])
    writer.writerow(data_demographics)
  
  # claims
  # today's date since this is not data from a healthcare facility
  admitDate = date.today().strftime("%d/%m/%Y")
  # this will be empty for all instances since this is not data from a healthcare facility
  dischargeDate = ""
  # flag will always be false since this is not data from a healthcare facility
  erVisit = 0 
  # flag will always be false since this is not data from a healthcare facility
  inpatient = 0
  #ICD10 codes
  dx = dx.replace("'", '')
  dx = dx.replace("[", '')
  dx = dx.replace("]", '')
  dx_list = dx.split(",")
  
  data_claims = [personid, admitDate, dischargeDate, erVisit] + dx_list
  
  with open('claims.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["personId","claimId","admitDate","dischargeDate","erVisit","inpatient","dx1","dx2","dx3","dx4","dx5","dx6","dx7","dx8","dx9","dx10","dx11","dx12","dx13","dx14","dx15"])
    writer.writerow(data_claims)

  with open('predictions.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["personId","prediction","risk_score","pos_factors_1","pos_patient_values_1","pos_shap_scores_1","pos_factors_2","pos_patient_values_2","pos_shap_scores_2","pos_factors_3","pos_patient_values_3","pos_shap_scores_3","pos_factors_4","pos_patient_values_4","pos_shap_scores_4","pos_factors_5","pos_patient_values_5","pos_shap_scores_5","pos_factors_6","pos_patient_values_6","pos_shap_scores_6","pos_factors_7","pos_patient_values_7","pos_shap_scores_7","pos_factors_8","pos_patient_values_8","pos_shap_scores_8","pos_factors_9","pos_patient_values_9","pos_shap_scores_9","pos_factors_10","pos_patient_values_10","pos_shap_scores_10","neg_factors_1","neg_patient_values_1","neg_shap_scores_1","neg_factors_2","neg_patient_values_2","neg_shap_scores_2","neg_factors_3","neg_patient_values_3","neg_shap_scores_3","neg_factors_4","neg_patient_values_4","neg_shap_scores_4","neg_factors_5","neg_patient_values_5","neg_shap_scores_5","neg_factors_6","neg_patient_values_6","neg_shap_scores_6","neg_factors_7","neg_patient_values_7","neg_shap_scores_7","neg_factors_8","neg_patient_values_8","neg_shap_scores_8","neg_factors_9","neg_patient_values_9","neg_shap_scores_9","neg_factors_10","neg_patient_values_10","neg_shap_scores_10"])
  
  return redirect(url_for('prediction'))

@app.route("/prediction")

def prediction():
  predict.do_run_claims("demographics.csv","claims.csv","predictions.csv","xgboost_all_ages",pd.to_datetime(datetime.today().isoformat()))
  with open('predictions.csv', 'r') as file:
    csvreader = csv.reader(file)
    header = []
    data = []
    header = next(csvreader)
    data = next(csvreader)
    risk_score = data[2]
  return "%s" % risk_score
