import csv
import uuid
from datetime import date

# generates random id to link to "claims" file
personid = str(uuid.uuid4())
personid = personid.replace('-', '')
personid = personid[0:16]
# demographics 
age = input("Input your age:\n")
# gender is binary with 0 being female and 1 being male
gender = input("Select your gender:\n0 for female\n1 for male\n")

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
# ICD10 codes
# dx1, dx2, dx3, dx4, dx5, dx6, dx7, dx8, dx9, dx10 = ("Enter all the codes that correspond to a condition that applies to you, separated by a whitespace:\nZ333 - Pregnancy\nZ572 - Occupational exposure to dust\nZ48813 - Surgery on the respiratory\nZ559 - Dyslexia or other learning difficulty\nI130 - Chronic Kidney Disease\nD56 - Thalassemia\nE66 - Obesity\nF41 - Anxiety\nK58 - Irritable Bowel Syndrome\nL20 - Atopic Dermatitis ")
dx = input("Enter all the codes that correspond to a condition that applies to you, separated by a whitespace:\nZ333 - Pregnancy\nZ572 - Occupational exposure to dust\nZ48813 - Surgery on the respiratory\nZ559 - Dyslexia or other learning difficulty\nI130 - Chronic Kidney Disease\nD56 - Thalassemia\nE66 - Obesity\nF41 - Anxiety\nK58 - Irritable Bowel Syndrome\nL20 - Atopic Dermatitis ")

dx_list = dx.split()

data_claims = [personid, admitDate, dischargeDate, erVisit] + dx_list

with open('claims.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["personId","claimId","admitDate","dischargeDate","erVisit","inpatient","dx1","dx2","dx3","dx4","dx5","dx6","dx7","dx8","dx9","dx10","dx11","dx12","dx13","dx14","dx15"])
    writer.writerow(data_claims)

with open('predictions.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["personId","prediction","risk_score","pos_factors_1","pos_patient_values_1","pos_shap_scores_1","pos_factors_2","pos_patient_values_2","pos_shap_scores_2","pos_factors_3","pos_patient_values_3","pos_shap_scores_3","pos_factors_4","pos_patient_values_4","pos_shap_scores_4","pos_factors_5","pos_patient_values_5","pos_shap_scores_5","pos_factors_6","pos_patient_values_6","pos_shap_scores_6","pos_factors_7","pos_patient_values_7","pos_shap_scores_7","pos_factors_8","pos_patient_values_8","pos_shap_scores_8","pos_factors_9","pos_patient_values_9","pos_shap_scores_9","pos_factors_10","pos_patient_values_10","pos_shap_scores_10","neg_factors_1","neg_patient_values_1","neg_shap_scores_1","neg_factors_2","neg_patient_values_2","neg_shap_scores_2","neg_factors_3","neg_patient_values_3","neg_shap_scores_3","neg_factors_4","neg_patient_values_4","neg_shap_scores_4","neg_factors_5","neg_patient_values_5","neg_shap_scores_5","neg_factors_6","neg_patient_values_6","neg_shap_scores_6","neg_factors_7","neg_patient_values_7","neg_shap_scores_7","neg_factors_8","neg_patient_values_8","neg_shap_scores_8","neg_factors_9","neg_patient_values_9","neg_shap_scores_9","neg_factors_10","neg_patient_values_10","neg_shap_scores_10"])
    
