import pandas as pd
import numpy as np
import streamlit as st
import pickle


st.write("<h1 style='text-align: center;'>Welcome to Insurance Prediction !</h1>", unsafe_allow_html=True)
st.image('image.jpg')

age = st.slider('Choose an age',0,100)
job = st.selectbox('Choose a job',['management', 'technician', 'entrepreneur', 'blue-collar',
       'retired', 'admin.', 'services', 'self-employed',
       'unemployed', 'housemaid', 'student'])
marital = st.selectbox('Choose a marital status',['married', 'single', 'divorced'])
education = st.selectbox('Choose an Education',['tertiary', 'secondary','primary'])
day = st.slider('Choose a day of call',1,31)
month = st.selectbox('Choose a month of call',['may', 'jun', 'jul', 'aug', 'oct', 'nov', 'dec', 'jan', 'feb',
       'mar', 'apr', 'sep'])
dur = st.number_input('Give a duration of call in seconds')
calls = st.slider('Choose number of calls',1,100)

dur = int(dur)
list =[age,day,dur,calls]
if job == 'management':
    list.insert(1,10)
if job == 'entrepreneur':
    list.insert(1,0)
if job == 'housemaid':
    list.insert(1,1)
if job == 'unemployed':
    list.insert(1,2)
if job == 'self-employed':
    list.insert(1,3)
if job == 'retired':
    list.insert(1,4)
if job == 'services':
    list.insert(1,5)
if job == 'student':
    list.insert(1,6)
if job == 'blue-collar':
    list.insert(1,7)
if job == 'admin.':
    list.insert(1,8)
if job == 'technician':
    list.insert(1,9)

if marital == 'divorced':
    list.insert(2,0)
if marital == 'single':
    list.insert(2,1)
if marital == 'married':
    list.insert(2,2)
   
if education == 'primary':
    list.insert(3,0)
if education == 'secondary':
    list.insert(3,1)
if education == 'tertiary':
    list.insert(3,2)

if month == 'dec':
    list.insert(5,0)
if month == 'jan':
    list.insert(5,1)
if month == 'mar':
    list.insert(5,2)
if month == 'sep':
    list.insert(5,3)
if month == 'oct':
    list.insert(5,4)
if month == 'nov':
    list.insert(5,5)
if month == 'feb':
    list.insert(5,6)
if month == 'jul':
    list.insert(5,7)
if month == 'jun':
    list.insert(5,8)
if month == 'aug':
    list.insert(5,9)
if month == 'apr':
    list.insert(5,10)
if month == 'may':
    list.insert(5,11)

with open('scale.pkl', 'rb') as f:
    scaler = pickle.load(f)
    
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
    
test = scaler.transform([list])
 
if st.button('predict'):
    
    prediction = model.predict(test)
    if prediction == [1]:
        st.write('Yes')
        st.image('thumbs_up.gif')
    if prediction == [0]:
        st.write('Sorry,No')
        st.image('no.gif')





