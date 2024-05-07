import joblib
import sklearn
from fastapi import FastAPI, HTTPException , APIRouter
import uvicorn
from pydantic import BaseModel
from typing import List
import pandas as pd
import os
import mlflow

class CoverType(BaseModel):
    race: List[str]=['Caucasian']
    gender: List[str]=['Female']
    age: List[str]=['[80-90)']
    admission_type_id: List[float]=[1]
    discharge_disposition_id: List[float]=[1]
    admission_source_id: List[float]=[7]
    metformin: List[str]=['Steady']
    repaglinide: List[str]=['No']
    nateglinide: List[str]=['No']
    chlorpropamide: List[str]=['No']
    glimepiride: List[str]=['No']
    acetohexamide: List[str]=['No']
    glipizide: List[str]=['No']
    glyburide: List[str]=['Steady']
    tolbutamide: List[str]=['No']
    pioglitazone: List[str]=['No']
    rosiglitazone: List[str]=['No']
    acarbose: List[str]=['No']
    miglitol: List[str]=['No']
    troglitazone: List[str]=['No']
    tolazamide: List[str]=['No']
    insulin: List[str]=['No']
    glyburide_metformin: List[str]=['No']
    glipizide_metformin: List[str]=['No']
    metformin_rosiglitazone: List[str]=['No']
    metformin_pioglitazone: List[str]=['No']
    change: List[str]=['Ch']
    diabetesMed: List[str]=['Yes']
    diag_1: List[float]=[435]
    diag_2: List[float]=[491]
    diag_3: List[float]=[428]
    time_in_hospital: List[float]=[10]
    num_lab_procedures: List[float]=[45]
    num_procedures: List[float]=[0]
    num_medications: List[float]=[14]
    number_outpatient: List[float]=[0]
    number_emergency: List[float]=[0]
    number_inpatient: List[float]=[0]
    number_diagnoses: List[float]=[9]
app = FastAPI()

def decode_input(input):
    input_dict=dict(input)
    df = pd.DataFrame.from_dict(input_dict)
    categorical_features = [
    'race', 'gender', 'age', 
    'admission_type_id','discharge_disposition_id', 
    'admission_source_id','metformin', 'repaglinide', 
    'nateglinide', 'chlorpropamide', 'glimepiride', 'acetohexamide', 'glipizide',
    'glyburide', 'tolbutamide', 'pioglitazone', 'rosiglitazone', 'acarbose',
    'miglitol', 'troglitazone', 'tolazamide', 'insulin', 'glyburide_metformin', 
    'glipizide_metformin', 'metformin_rosiglitazone', 'metformin_pioglitazone',
    'change', 'diabetesMed', 'diag_1', 'diag_2','diag_3'
    ]

    numerical_features = ['time_in_hospital', 'num_lab_procedures', 'num_procedures', 'num_medications', 
                        'number_outpatient', 'number_emergency','number_inpatient', 'number_diagnoses']
                        
    all_features = categorical_features + numerical_features
    
    df = df[all_features]
    print(df)
    return df

@app.post("/predict/{model_name}")
def predict_model(input_data : CoverType,model_name: str = "DecisionTreeClassifier"):
    os.environ['MLFLOW_S3_ENDPOINT_URL'] = "http://minio:9000"
    os.environ['AWS_ACCESS_KEY_ID'] = 'admin'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'supersecret'
    mlflow.set_tracking_uri("http://10.43.101.151:8087")
    #mlflow.set_experiment("mlflow_tracking_examples")
    model_production_uri = "models:/best_{model_name}@production".format(model_name=model_name)
    loaded_model = mlflow.pyfunc.load_model(model_uri=model_production_uri)
    decoded_data = decode_input(input_data)
    prediction = loaded_model.predict(decoded_data)
    prediction_list = prediction.tolist()
    
    return {"model_used": model_name, "prediction":prediction_list}