
# 1. Library imports
import uvicorn
from fastapi import FastAPI
# from Credit import Credit
from pydantic import BaseModel
import joblib


app = FastAPI()
#Credt Scoring
Model1 = 'Kelayakan.joblib'
classifier = joblib.load(Model1)

Model2 = 'Pemberian_dana.joblib'
classifier2 = joblib.load(Model2)

from fastapi import FastAPI



# Load your trained model


app = FastAPI()

class Credit(BaseModel):
    isMustahiq: int
    UMR_Provinsi: int
    Untung_Kotor: int
    Pengeluaran: int
    Untung_Bersih: int
    Presentase_Serapan_Pasar: float
    Sustain: int
    isInfra: int
    isIZIN: int
    Nominal_Kebutuhan_Alat: int

@app.post("/predict/")
async def predict_credit_score(data: Credit):
    # Extract the input features from the request data
    features = [
        data.isMustahiq,
        data.UMR_Provinsi,
        data.Untung_Kotor,
        data.Pengeluaran,
        data.Untung_Bersih,
        data.Presentase_Serapan_Pasar,
        data.Sustain,
        data.isInfra,
        data.isIZIN,
        data.Nominal_Kebutuhan_Alat
    ]
    
    # Make a prediction using your model
    prediction = classifier.predict([features])
    if prediction[0] == 1:
        prediction1 = classifier2.predict([features])
        return {"prediction": "Layak", "loan_amount": int(prediction1[0])}
    else:
        return {"prediction": "Tidak Layak" ,"loan_amount": 0}


if __name__ == '__app__':
    uvicorn.run(app, host='127.0.0.2', port=8000)


#uvicorn app:app --reload





