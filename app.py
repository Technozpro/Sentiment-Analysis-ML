# It is a magic command to create a .py file
import streamlit as st
import joblib
import pandas as pd
st.title('Sentiment Analysis Deployment')
test_model = joblib.load('SentimentAnalysis')
ip = st.text_input('Enter your message')
op = test_model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
