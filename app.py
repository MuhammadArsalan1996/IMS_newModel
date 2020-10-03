# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 15:47:38 2020
@author: Muhammad Arsalan
"""



import numpy as np
import pickle
import pandas as pd

import streamlit as st 

from PIL import Image


@app.route('/')
def welcome():
    return "Welcome All"
@app.route('/predict',methods=["Get"])
def predict_note_authentication(Diabetes_Type1,Diabetes_Type2,liverDisease
,heartDisease, kidneyDisease,Flu,Fever,LowBP,HighBP):

   
    prediction=IMS_model.predict([[Diabetes_Type1,Diabetes_Type2,liverDisease
,heartDisease, kidneyDisease,Flu,Fever,LowBP,HighBP]])
    print(prediction)
    return prediction



def main():
    st.title("Select your Disease if necessary")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
   
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Diabetes_Type1 = st.checkbox("Diabetes_Type1")
    if Diabetes_Type1:
     st.checkbox("yes", value = True,key=0);
    Diabetes_Type2 = st.checkbox("Diabetes_Type2")
    if Diabetes_Type2:
     st.checkbox("yes", value = True,key=1)
    liverDisease = st.checkbox("liverDisease")
    if liverDisease:
     st.checkbox("yes", value = True,key=2)
    heartDisease = st.checkbox("heartDisease")
    if heartDisease:
     st.checkbox("yes", value = True,key=3)
    kidneyDisease = st.checkbox("kidneyDisease")
    if kidneyDisease:
     st.checkbox("yes", value = True,key=4)
    Flu = st.checkbox("Flu")
    if Flu:
     st.checkbox("yes", value = True,key=5)
    Fever = st.checkbox("Fever" )
    if Fever:
     st.checkbox("yes", value = True,key=6)
    LowBP = st.checkbox("LowBP" )
    if LowBP:
     st.checkbox("yes", value = True,key=7)
    HighBP= st.checkbox("HighBP")
    if HighBP:
     st.checkbox("yes", value = True,key=8)
    result=""
    if st.button("Predict"):
      result=predict_note_authentication(Diabetes_Type1,Diabetes_Type2,liverDisease,heartDisease, kidneyDisease,Flu,Fever,LowBP,HighBP)
    st.success('Recommended {}'.format(result)) 
   
 


if __name__=='__main__':
    main()
