# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 09:49:07 2024

@author: suprl
"""

import pandas as pd
import src.modules.custom_functions as fn



data_dict = {'aapl': pd.DataFrame()}


apple = pd.read_csv('AAPL.csv')
data_dict['AAL'] = pd.read_csv()

import os

list_stocks = os.listdir('Input/Data_and_Features')

data_dict = {}

for ticker in list_stocks:
    data_dict[ticker] = pd.read_csv()
    
    

fn.custom_chart(df, sve_fig)

fn.custom_chart(df = dict_data['AAPL'], file_name)
