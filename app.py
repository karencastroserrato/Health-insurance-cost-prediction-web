import streamlit as st 
import joblib

def main():

    html_temp = """
    <div style = "background-color: lightblue; padding:16px; text-align:center">
    <h1 style = "color: black"> Health Insurance Cost Prediction </h1>
   """

    st.markdown(html_temp, unsafe_allow_html=True)

    model = joblib.load('model_joblib_gb')

    entry1 = st.slider('Select your age', 18, 100)
    s1 = st.selectbox('Select  your gender', ('Male', 'Female'))
    if s1=='Male':
        entry2 = 1
    else:
        entry2 = 0
    entry3 = st.number_input('Enter your BMI value')
    entry4 = st.slider('Select  your number of childrens', 0, 4)
    s2 = st.selectbox('Are you smoker?', ('Yes', 'No'))
    if s2=='Yes':
        entry5 = 1
    else:
        entry5=0
    entry6 = st.slider('Select  your region: SW(0), SE(1), NW(2), NE(3)', 0, 3)

    if st.button('Predict'):
        pred = model.predict([[entry1,entry2,entry3,entry4,entry5,entry6]])
        st.balloons()
        st.success('Your Health Insurance Cost Prediction is {}'.format(round(pred[0],2)))

if __name__=='__main__':
    main()
