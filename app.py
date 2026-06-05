# load libraries
import streamlit as st
from src.predict import predict_churn

# set page configuration
st.set_page_config(page_title="Bank Customer System",
                   page_icon="💰",
                   layout="centered"
                   )
st.title("Bank Deposit Predictive System")
st.markdown("**Predict whether a Bank Customer will subscribe to a TERM DEPOSIT using Machine Learning**")

st.divider()

st.subheader("📊 Customer Information Input")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=95)
    job = st.selectbox("Job", [
        "admin.", "blue-collar", "entrepreneur", "housemaid",
        "management", "retired", "self-employed", "services",
        "student", "technician", "unemployed", "unknown"  
    ])
    marital = st.selectbox("Marital", [
        "divorced", "married", "single"
    ])
    education = st.selectbox("Education", [
        "primary", "secondary", "tertiary", "unknown"
    ])
    default = st.selectbox("Credit in Default?", [
        "yes", "no"
    ])
    balance = st.number_input("Account Balance", value=1000)
    housing = st.selectbox("Housing Loan", [
        "yes", "no"
    ])
    loan = st.selectbox("Personal Loan", [
        "yes", "no"
    ])

with col2:
    contact = st.selectbox("Contact Type", [
        "cellular", "telephone", "unknown"
    ])
    day = st.number_input("Last Contact Day", 
                          min_value=1, max_value=31
                          )
    month = st.selectbox("Month", [
        "jan", "feb", "mar", "apr", "may", "june",
        "jul", "aug", "sep", "oct", "nov", "dec"
    ])
    duration = st.number_input("Call Duration (seconds)", value=4918)
    campaign = st.number_input("Number of Contacts", value=63)
    pdays = st.number_input("Days Since Last Contact (-1 if never)", value=536)
    previous = st.number_input("Previous Contacts", value=275)
    poutcome = st.selectbox("Previous Outcome", [
        "failure", "success", "unknown", "other"
    ])

if st.button("Predict Bank Customer Subscription DEPOSIT"):
    input_data = {
        "age" : age,
        "job" : job,
        "marital" : marital,
        "education" : education,
        "default" : default,
        "balance" : balance,
        "housing" : housing,
        "loan" : loan,
        "contact" : contact,
        "day" : day,
        "month" : month,
        "duration" : duration,
        "campaign" : campaign,
        "pdays" : pdays,
        "previous" : previous,
        "poutcome" : poutcome
    }

    result = predict_churn([input_data])

    st.subheader("Bank Customer TERM DEPOSIT result")
    st.success((result["Term Deposit Prediction"]))
    st.success((result["Term Deposit Probability"]))

# age	job	marital	education
# 	default	balance	housing	loan	
# contact	day	month	duration	
# campaign	pdays	previous	poutcome

# 58,management,married,tertiary,no,2143,yes,no,unknown,5,may,261,1,-1,0,unknown - NO
# 21,student,single,secondary,no,2488,no,no,telephone,12,jan,661,2,92,1,success - YES