# app.py
import streamlit as st # type: ignore
import pandas as pd
import joblib  # or joblib
from sklearn.linear_model import LinearRegression

# -----------------------------
# Load trained model
# -----------------------------
# Make sure you have saved your trained model as 'model.pkl'
# Example: 
# import pickle
# pickle.dump(model, open("model.pkl", "wb"))

model = joblib.load("model.joblib")

# -----------------------------
# App Title
# -----------------------------
st.title("🎓 Student Academic Performance Predictor")

st.write("""
Enter the student details below to predict their academic performance.
""")

# -----------------------------
# Input Widgets
# -----------------------------
gender = st.selectbox("Gender", ["Male", "Female"])
study_hours = st.number_input("Study Hours per Week", min_value=0, max_value=100, value=10)
attendance = st.slider("Attendance Rate (%)", 0, 100, 80)
past_scores = st.number_input("Past Exam Scores", min_value=0, max_value=100, value=75)
internet_access = st.radio("Internet Access at Home", ["No", "Yes"])
extracurricular = st.radio("Extracurricular Activities", ["No", "Yes"])
st.write("""Parents Education Level""")
bachelors = st.checkbox("Bachelors Degree")
masters = st.checkbox("Masters Degree")
phd = st.checkbox("PhD")

# -----------------------------
# Convert inputs to model format
# -----------------------------
# Map categorical variables
gender_val = 0 if gender == "Male" else 1
internet_val = 0 if internet_access == "No" else 1
extracurricular_val = 0 if extracurricular == "No" else 1
bachelors_val = 1 if bachelors else 0
masters_val = 1 if masters else 0
phd_val = 1 if phd else 0

# Create DataFrame for model
input_df = pd.DataFrame([[gender_val, study_hours, attendance, past_scores,
                        internet_val, extracurricular_val,
                        bachelors_val, masters_val, phd_val]],
                        columns=['Gender','Study_Hours_per_Week','Attendance_Rate',
                                'Past_Exam_Scores','Internet_Access_at_Home',
                                'Extracurricular_Activities','Bachelors','Masters','PhD'])

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Performance"):
    prediction = model.predict(input_df)
    st.success(f"Marks at Final Exam: {prediction[0]:.2f}")

