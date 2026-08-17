import streamlit as st
import pandas as pd
import joblib

st.title("Bank Deposit Prediction System")

st.write("This application predicts whether a customer will subscribe to a term deposit.")

age = st.number_input("Age", min_value=18, max_value=100, value=35)
balance = st.number_input("Balance", value=1000)
day = st.number_input("Day", min_value=1, max_value=31, value=15)
duration = st.number_input("Duration", value=300)
campaign = st.number_input("Campaign", value=1)
pdays = st.number_input("Pdays", value=-1)
previous = st.number_input("Previous", value=0)

model = joblib.load("random_forest.pkl")

if st.button("Predict"):

    input_data = pd.DataFrame([[
        age,0,0,0,0,
        balance,0,0,0,
        day,0,duration,
        campaign,pdays,
        previous,0
    ]],
    columns=[
        'age','job','marital','education',
        'default','balance','housing',
        'loan','contact','day','month',
        'duration','campaign','pdays',
        'previous','poutcome'
    ])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Customer is likely to subscribe.")
    else:
        st.error("Customer is not likely to subscribe.")