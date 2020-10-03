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
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Loading ML Model
IMS_model = pickle.load(open('ims.pkl', 'rb'))

@app.route('/')
def welcome():
    return "Welcome All"

        #Mobile App Api
@app.route('/predict_api',methods=['GET', 'POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''   
    data = request.get_json(force=True)
    final_features = [np.array(data)]
    recommended  =IMS_model.predict(final_features)
    recommended2 =IMS_model.predict(final_features)
    recommended3 =IMS_model.predict(final_features)
    recommended4 =IMS_model.predict(final_features)
    recommended5 =IMS_model.predict(final_features)
   

    
    return jsonify(recommended=recommended[0][0],recommended2=recommended2[0][1],recommended3=recommended3[0][2],recommended4=recommended4[0][3],recommended5=recommended5[0][4])
     

if __name__=='__main__':
    main()
