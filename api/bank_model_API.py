# load packages
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# instance of fastapi
app = FastAPI(
    message = "API Running",
    title="Bank Customer Term Deposit API"
)

# basemodel class
class model_input(BaseModel):
    age : int
    job : str
    marital : str
    education : str
    default : str
    balance : int
    housing : str
    loan : str
    contact : str
    day : int
    month : str
    duration : int
    campaign : int
    pdays : int
    previous : int
    poutcome : str

# load the saved model
# model = joblib.load(open('/Users/macbookpro/Desktop/End-to-End Projects/bank_customer/model/bank_model.pkl', 'rb'))
with open('/Users/macbookpro/Desktop/End-to-End Projects/bank_customer/model/bank_model.pkl', 'rb') as f:
    model = joblib.load(f)

# create endpoint
@app.post("/bank_customer")

# user inputs parameters
def cust_pred(input_parameters : model_input):
    bank_data = pd.DataFrame([{
        "age" : input_parameters.age,
        "job" : input_parameters.job,
        "marital" : input_parameters.marital,
        "education": input_parameters.education,
        "default" : input_parameters.default,
        "balance" : input_parameters.balance,
        "housing" : input_parameters.housing,
        "loan" : input_parameters.loan,
        "contact" : input_parameters.contact,
        "day" : input_parameters.day,
        "month" : input_parameters.month,
        "duration" : input_parameters.duration,
        "campaign" : input_parameters.campaign,
        "pdays" : input_parameters.pdays,
        "previous" : input_parameters.previous,
        "poutcome" : input_parameters.poutcome
}])

# previous

    # model prediction
    predictions = model.predict(bank_data)[0]

    # probability
    probability = max(
        model.predict_proba(bank_data)[0]
    )

    # prediction logic
    if predictions == "yes":
        return {
            "prediction": "YES, This Customer MADE a Term Deposit"
        }
    else:
        return {
        "prediction": "NO, This Customer DID NOT Make a Term Deposit"
    }
    
    # if predictions == "yes":
    #     return "YES, This Customer MADE a Term Deposit"
    # else:
    #     return "NO, This Customer DID NOT Made a Term Deposit"