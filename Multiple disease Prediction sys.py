
import pickle 
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

diabetes_model = pickle.load(open('C:/Users/yashb/Desktop/Multiple Disease Prediction System/SAV files project -2/diabetes_model.sav', 'rb'))
heartdisease_model = pickle.load(open('C:/Users/yashb/Desktop/Multiple Disease Prediction System/SAV files project -2/heartdisease_model (1).sav', 'rb'))
parkinsons_model = pickle.load(open('C:/Users/yashb/Desktop/Multiple Disease Prediction System/SAV files project -2/parkinsons_model.sav', 'rb'))

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System', 
                           ['Diabetes Prediction', 
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                           
                           icons = ['activity', 'heart', 'person'],
                           default_index = 0)
    
    
    
    
    
# diabetes Prediction
if (selected == 'Diabetes Prediction'):
    st.title('Diabetes Prediction')
    
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose level')
        
    with col3:
        BloodPressure = st.text_input('Blood pressure Level')
        
    with col1:
        SkinThickness = st.text_input('Skin thickness Value')
        
    with col2:
        Insulin = st.text_input('Insulin level')
        
    with col3:
        BMI =  st.text_input('BMI value')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        
    with col2:
        Age  = st.text_input('Age of a Person')
    

    
    diab_diagnosis = ''
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    
        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is Diabetic'
        else:
            diab_diagnosis = 'The person is NOT Diabetic'
            
    st.success(diab_diagnosis)
    
    
    
    
    
# heart disease prediction     
if (selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Prediction')

    col1, col2, col3 = st.columns(3)
    with col1:
        male  = st.text_input('Gender (1-male, 0-female)')
    with col2:
        age  = st.text_input('Age')
    with col3:
        cigsPerDay = st.text_input('Cigarettes per Day')
    with col1:
        prevalentHyp = st.text_input('Prevalent Hypertension (1-Yes, 0-No)')
    with col2:
        diabetes = st.text_input('Diabetic (1-Yes, 0-No)')
    with col3:
        sysBP = st.text_input('Systolic BP')
    with col1:
        BMI = st.text_input('BMI')

    heart_diagnosis = ''

    if st.button('Heart Disease Result'):
        try:
        
            male = float(male)
            age = float(age)
            cigsPerDay = float(cigsPerDay)
            prevalentHyp = float(prevalentHyp)
            diabetes = float(diabetes)
            sysBP = float(sysBP)
            BMI = float(BMI)

       
            heart_prediction = heartdisease_model.predict([[male, age, cigsPerDay, prevalentHyp, diabetes, sysBP, BMI]])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person has heart disease'
            else:
                heart_diagnosis = 'The person does NOT have heart disease'

        except ValueError:
            heart_diagnosis = 'Please enter valid numeric values.'

    st.success(heart_diagnosis)



# Parkinsons Prediction
if selected == 'Parkinsons Prediction':
    st.title('Parkinson’s Disease Prediction')

    col1, col2, col3 = st.columns(3)

    
    with col1:
        MDVP_Fo_Hz = st.text_input('MDVP:Fo(Hz) value')
    with col2:
        MDVP_Fhi_Hz = st.text_input('MDVP:Fhi(Hz) value')
    with col3:
        MDVP_Flo_Hz = st.text_input('MDVP:Flo(Hz) value')
    with col1:
        MDVP_Jitter_Percent = st.text_input('MDVP:Jitter(%) value')
    with col2:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs) value')
    with col3:
        MDVP_RAP = st.text_input('MDVP:RAP value')
    with col1:
        MDVP_PPQ = st.text_input('MDVP:PPQ value')
    with col2:
        Jitter_DDP = st.text_input('Jitter:DDP value')
    with col3:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer value')
    with col1:
        MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer(dB) value')
    with col2:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3 value')
    with col3:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5 value')
    with col1:
        MDVP_APQ = st.text_input('MDVP:APQ value')
    with col2:
        Shimmer_DDA = st.text_input('Shimmer:DDA value')
    with col3:
        NHR = st.text_input('NHR value')
    with col1:
        HNR = st.text_input('HNR value')
    with col2:
        RPDE = st.text_input('RPDE value')
    with col3:
        DFA = st.text_input('DFA value')
    with col1:
        spread1 = st.text_input('spread1 value')
    with col2:
        spread2 = st.text_input('spread2 value')
    with col3:
        D2 = st.text_input('D2 value')
    with col1:
        PPE = st.text_input('PPE value')

    parkinsons_diagnosis = ""

    if st.button('Parkinson’s Result'):
        try:
            
            features = np.array([
                float(MDVP_Fo_Hz), float(MDVP_Fhi_Hz), float(MDVP_Flo_Hz), 
                float(MDVP_Jitter_Percent), float(MDVP_Jitter_Abs), float(MDVP_RAP), 
                float(MDVP_PPQ), float(Jitter_DDP), float(MDVP_Shimmer), 
                float(MDVP_Shimmer_dB), float(Shimmer_APQ3), float(Shimmer_APQ5), 
                float(MDVP_APQ), float(Shimmer_DDA), float(NHR), 
                float(HNR), float(RPDE), float(DFA), 
                float(spread1), float(spread2), float(D2), float(PPE)
            ]).reshape(1, -1)

          
            parkinsons_prediction = parkinsons_model.predict(features)

            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = 'The person has Parkinson’s disease'
            else:
                parkinsons_diagnosis = 'The person does NOT have Parkinson’s disease'

        except ValueError:
            parkinsons_diagnosis = "Please enter valid numeric values for all fields."

    st.success(parkinsons_diagnosis)

            
        
        

                        