# load libraries
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import uvicorn
import json
from pyngrok import ngrok
from fastapi.middleware.cors import CORSMiddleware

# instance of api
app = FastAPI()

# origins
origins = ['*']

# app middlewares
CORSMiddleware,
allow_origins='origins',
allow_credentials=True,
allow_methods=['*'],
allow_headers=['*']

# basemodel inputs
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
    previuos : int
    poutcome : str

# load model file
model = joblib.load(open('/Users/macbookpro/Desktop/End-to-End Projects/bank_customer/model/bank_model.pkl', 'rb'))
# with open('/Users/macbookpro/Desktop/End-to-End Projects/bank_customer/model/bank_model.pkl') as f:
#     model = joblib.load(f)

# url endpoint
@app.post('/bank_customer')

# function of user input
def cust_pred(input_parameters : model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    age = input_dictionary['age']
    job = input_dictionary['job']
    marital = input_dictionary['marital']
    education = input_dictionary['education']
    default = input_dictionary['default']
    balance = input_dictionary['balance']
    housing = input_dictionary['housing']
    loan = input_dictionary['loan']
    contact = input_dictionary['contact']
    day = input_dictionary['day']
    month = input_dictionary['month']
    duration = input_dictionary['duration']
    campaign = input_dictionary['campaign']
    pdays = input_dictionary['pdays']
    previous = input_dictionary['previous']
    poutcome = input_dictionary['poutcome']    

# store user inputs in a array
    input_list = [
        age,
        job,
        marital,
        education,
        default,
        balance,
        housing,
        loan,
        contact,
        day,
        month,
        duration,
        campaign,
        pdays,
        previous,
        poutcome
    ]

# model prediction
    prediction = model.predict([input_list])

# prediction logic
    if prediction["yes"] == "yes":
        return "YES, This Customer MADE a Term Deposit"
    else:
        return "NO, This Customer DID NOT Made a Term Deposit"

# ngrok auth-token
NGROK_AUTH_TOKEN = "3EjA16TFGlBbB0QMoVHDUW5ac0t_34wyo9UEpojwKpfYuEcwn"
# set token
ngrok.set_auth_token(NGROK_AUTH_TOKEN)
# connect ngrok
ngrok_tunnel = ngrok.connect()
# print ngrok url
print('Public URL: ', ngrok_tunnel.public_url)
# run uvicorn app
uvicorn.run(app, port=8000)