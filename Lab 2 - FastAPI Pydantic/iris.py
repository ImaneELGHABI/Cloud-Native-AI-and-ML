# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import uvicorn

# Define a request schema
class IrisModelInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

app = FastAPI()

model = joblib.load('iris_model1.joblib')


@app.post("/predict")
def predict(input_data: IrisModelInput):
    # Convert input data to a list for prediction
    test_data = [[
        input_data.sepal_length,
        input_data.sepal_width,
        input_data.petal_length,
        input_data.petal_width
    ]]
    prediction = model.predict(test_data)
    return {"prediction": int(prediction[0])}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8765)
