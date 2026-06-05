# load packages
import pandas as pd
import joblib

# load the trained pipeline
# with open('/Users/macbookpro/Desktop/End-to-End Projects/bank_customer/model/bank_model.pkl', 'rb') as f:
#     model = joblib.load(f)
model = joblib.load("model/bank_model.pkl")

# function to predict term_deposit
def predict_churn(input_data):

    bank_data = pd.DataFrame(input_data)

    prediction = model.predict(bank_data)[0]
    probability = model.predict_proba(bank_data)[0][1]

    return {
        "Term Deposit Prediction": 
        "YES, This Customer MADE a Term Deposit" 
        if prediction == "yes" 
        else "NO, This Customer DID NOT Made a Term Deposit",
        "Term Deposit Probability": 
        round(float(probability),2)
    }