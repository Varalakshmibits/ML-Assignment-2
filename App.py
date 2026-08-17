import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("random_forest.pkl")

st.title("Bank Deposit Prediction")

st.write("Enter customer details to predict whether the customer will subscribe to a term deposit.")

age = st.number_input("Age", min_value=18, max_value=100, value=35)
balance = st.number_input("Balance", value=1000)
day = st.number_input("Day", min_value=1, max_value=31, value=15)
duration = st.number_input("Duration", value=300)
campaign = st.number_input("Campaign", value=1)
pdays = st.number_input("Pdays", value=-1)
previous = st.number_input("Previous Contacts", value=0)

if st.button("Predict"):

    input_data = pd.DataFrame({
        'age':[age],
        'job':[0],
        'marital':[0],
        'education':[0],
        'default':[0],
        'balance':[balance],
        'housing':[0],
        'loan':[0],
        'contact':[0],
        'day':[day],
        'month':[0],
        'duration':[duration],
        'campaign':[campaign],
        'pdays':[pdays],
        'previous':[previous],
        'poutcome':[0]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Customer is likely to subscribe to the term deposit.")
    else:
        st.error("❌ Customer is unlikely to subscribe to the term deposit.")

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Customer is likely to subscribe.")
    else:
        st.error("Customer is not likely to subscribe.")
