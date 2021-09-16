import uvicorn
from fastapi import FastAPI
from promotion_prediction import PromotionPrediction
import pickle
from mapping import (
    edu_mapping, 
    gender_mapping, 
    mapping_dept_score,
    wilayah_mapping
)

app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier =pickle.load(pickle_in)

@app.get('/')
def index():
    return {'message':'This is My Employee Promotion Prediction'}

@app.post('/predict')
def predict_promotion(data:PromotionPrediction):
    data = data.dict()
    yes_no = {'YES':1 , 'NO':0}

    wilayah = wilayah_mapping.get(data['wilayah'])
    pendidikan = edu_mapping.get(data['pendidikan'])
    jenis_kelamin = gender_mapping.get(data['jenis_kelamin'])
    jumlah_training = data['jumlah_training']
    umur = data['umur']
    rating_tahun_lalu= data['rating_tahun_lalu']
    masa_kerja= data['masa_kerja']
    KPI = yes_no[data['KPI']]
    penghargaan = yes_no[data['penghargaan']]
    rata_rata_skor_training = data['rata_rata_skor_training']
    departemen = data['departemen']
    rata_rata_skor_training_departemen = mapping_dept_score[data['departemen']]
    perbandingan_skor_dengan_rata_rata_departemen = rata_rata_skor_training/rata_rata_skor_training_departemen
    akumulasi_skor = jumlah_training*rata_rata_skor_training
    # departemen
    Finance = 0
    HR = 0
    Legal = 0
    Operations = 0
    Procurement = 0
    RnD = 0
    SalesMarketing = 0
    Technology = 0
    if data['departemen'] == 'Finance':
        Finance = 1
    elif data['departemen'] == 'HR':
        HR = 1
    elif data['departemen'] == 'Legal':
        Legal = 1
    elif data['departemen'] == 'Operations':
        Operations = 1
    elif data['departemen'] == 'Procurement':
        Procurement = 1
    elif data['departemen'] == 'RnD':
        RnD = 1
    elif data['departemen'] == 'Sales Marketing':
        SalesMarketing = 1
    elif data['departemen'] == 'Technology':
        Technology = 1
        
    # rekrutment
    Sourcing = 0
    Other = 0 
    if data['rekrutmen'] == 'Sourcing':
        Sourcing = 1
    elif data['rekrutmen'] == 'Other':
        Other = 1

    data_pred = [[wilayah, pendidikan, jenis_kelamin, jumlah_training, umur,
       rating_tahun_lalu, masa_kerja, KPI, penghargaan,
       rata_rata_skor_training, rata_rata_skor_training_departemen,
       perbandingan_skor_dengan_rata_rata_departemen, akumulasi_skor,
       Finance, HR, Legal, Operations, Procurement, RnD,
       SalesMarketing, Technology,
       Other, Sourcing]]
    prediction = classifier.predict(data_pred)
    #print(prediction[0],'INIIIIIIIIIIIIII')
    if prediction[0] == 1:
        result = 'You will be promoted!'
    else:
        result = 'You will not be promoted'
    return {
        'prediction': result
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
