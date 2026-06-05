# load libraries
import json
import requests

# api endpoint url
url = "http://127.0.0.1:8000/bank_customer"

# model values
input_model_values = {
    'age' : 57,
    'job' : 'technician',
    'marital' : 'single',
    'education' : 'tertiary',
    'default' : 'no',
    'balance' : 3723,
    'housing' : 'yes',
    'loan' : 'yes',
    'contact' : 'unknown',
    'day' : 28,
    'month' : 'nov',
    'duration' : 568,
    'campaign' : 6,
    'pdays' : 183,
    'previous' : 2, #previous
    'poutcome' : 'unknown' #no
}

# dumps json from input
input_json = json.dumps(input_model_values)

# response from api url
response = requests.post(url, data=input_json)

# print response
print(response.text)