import streamlit as st
import pickle

st.title('Waiter Tips Prediction :heavy_dollar_sign: ')
model=pickle.load(open('tip.pkl','rb'))
total_bill=st.number_input('total_bill',1,50)
smoker_mapping = {'No': 0, 'Yes': 1}
smoker = st.selectbox('smoker', ['No', 'Yes'])
smoker_numeric = smoker_mapping[smoker]
size=st.number_input('size',1,10)
day_mapping = {'Sunday':0, 'Saturday':1, 'Thursday':2, 'Friday':3}
day = st.selectbox('day', ['Sunday', 'Saturday', 'Thursday', 'Friday'])
day_numeric = day_mapping[day]
sex_mapping = {'Male': 0, 'Female': 1}
sex = st.selectbox('sex', ['Male', 'Female'])
sex_numeric = sex_mapping[sex]
time_mapping = {'Dinner': 0, 'Lunch': 1}
time = st.selectbox('time', ['Dinner', 'Lunch'])
time_numeric = time_mapping[time]
if st.button('predict'):
    prediction=model.predict([[total_bill,smoker_numeric,size,day_numeric,sex_numeric,time_numeric]])
    prediction=prediction
    st.success(f'tip prediction:{prediction}')