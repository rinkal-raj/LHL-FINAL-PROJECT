import streamlit as st
import numpy as np
import pickle
import pandas as pd
import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)

# Load models and columns
with open('log_reg.pkl', 'rb') as f:
    log_reg = pickle.load(f)

with open('model_columns.pkl', 'rb') as f:
    model_columns = pickle.load(f)


def predict(json_data):
    try:
        query_ = pd.get_dummies(pd.DataFrame(json_data))
        query = query_.reindex(columns=model_columns, fill_value=0)

        prediction = log_reg.predict(query)
        result = "Patient does not have heart disease"
        if prediction[0] == 1:
            result = "Patient has heart disease"

        return prediction[0], result

    except Exception as e:
        return None, str(e)


def main():
    st.title('Heart Diseases Prediction')

    st.write("Welcome! Use this Streamlit App for Heart Diseases Prediction")

    st.text("Please Enter the Input Regarding Instruction")
    st.text("Please Enter in Sex Input  0 : Female and 1 : Male")
    st.text("Please Enter in Chest Pain Type Input  1 : ASY , 2 : ATA, 3 : NAP , 4 : TA")
    st.text("Please Enter in Resting ECG Input 0 : ST , 1 : Normal , 2 : LVH")
    st.text("Please Enter in Excersice Input 0 : Yes , 1 : No ")
    st.text("Please Enter in Fasting Blood Sugar Input 0 : Yes , 1 : No ")
    st.text("Please Enter in ST slope Input 1 : Up , 2 : Flat , 3: Down ")
    


    # Collect user input
    age = st.number_input('Age', min_value=1, max_value=120, value=30)
    sex = st.selectbox('Sex', [0, 1])
    chest_pain_type = st.number_input('Chest Pain Type', min_value=1, max_value=4, value=1)
    resting_bp = st.number_input('Resting BP', min_value=60, max_value=250, value=130)
    cholesterol = st.number_input('Cholesterol', min_value=100, max_value=500, value=200)
    fasting_bs = st.selectbox('Fasting Blood Sugar', [0, 1])
    resting_ecg = st.number_input('Resting ECG', min_value=0, max_value=2, value=0)
    max_hr = st.number_input('Max Heart Rate', min_value=50, max_value=250, value=150)
    exercise_angina = st.selectbox('Exercise Induced Angina', [0, 1])
    oldpeak = st.number_input('Oldpeak', min_value=0.0, max_value=10.0, value=0.0)
    st_slope = st.number_input('ST Slope', min_value=1, max_value=3, value=1)

    json_data = {
        "Age": age,
        "Sex": sex,
        "ChestPainType": chest_pain_type,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "RestingECG": resting_ecg,
        "MaxHR": max_hr,
        "ExerciseAngina": exercise_angina,
        "Oldpeak": oldpeak,
        "ST_Slope": st_slope,
    }

    # Get prediction
    if st.button('Predict'):
        prediction, result = predict([json_data])
        if prediction is not None:
            st.write(f"Prediction: {prediction}")
            st.write(f"Result: {result}")


if __name__ == "__main__":
    main()
