import streamlit as st
import joblib
import pandas as pd

# Load trained model and preprocessing objects
model = joblib.load('models/thyroid_recurrence_modell.pkl')
encoders = joblib.load("models/label_encoders.pkl")  # Label Encoders
scaler = joblib.load("models/scaler.pkl")  # StandardScaler

# Streamlit UI
st.title("Thyroid Cancer Recurrence Prediction")
st.write("Enter patient details to predict the likelihood of recurrence.")

st.write(model.estimator_)
# Input fields for the 7 selected features
adenopathy = st.selectbox("Adenopathy", ['No', 'Right', 'Extensive', 'Left', 'Bilateral', 'Posterior'])
risk = st.selectbox("Risk Level", ['Low', 'Intermediate', 'High'])
t_stage = st.selectbox("Tumor Size (T)", ['T1a', 'T1b', 'T2', 'T3a', 'T3b', 'T4a', 'T4b'])
n_stage = st.selectbox("Lymph Node Involvement (N)", ['N0', 'N1a', 'N1b'])
stage = st.selectbox("Cancer Stage", ['I', 'II', 'III', 'IVA', 'IVB'])
response = st.selectbox("Treatment Response", ['Excellent', 'Indeterminate', 'Biochemical Incomplete', 'Structural Incomplete'])

# Numerical input
age = st.number_input("Age", min_value=15, max_value=85)

# Convert inputs into a DataFrame
input_data = pd.DataFrame([[adenopathy, risk, t_stage, n_stage, stage, response, age]],
                          columns=['Adenopathy', 'Risk', 'T', 'N', 'Stage', 'Response', 'Age'])

# Encode categorical variables using stored encoders
for col in encoders.keys():
    input_data[col] = encoders[col].transform(input_data[col])

# Scale Age using StandardScaler
input_data['Age'] = scaler.transform(input_data[['Age']])
st.write(input_data)
# Make prediction
if st.button('Predict'):
    prediction = model.estimator_.predict(input_data)

    # Display result
    st.subheader("Prediction Result")
    st.write("Prediction: ", "Recurrence" if prediction[0] == 1 else "No Recurrence")
