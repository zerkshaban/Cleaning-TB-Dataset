#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 03:36:24 2020

@author: Zerk Shaban 

Goal State
  country  year    age sex  cases
0      AD  1996  15-24   f    1.0
1      AD  1996  15-24   m    0.0
2      AD  1996  25-34   f    1.0
3      AD  1996  25-34   m    0.0
4      AD  1996  35-44   f    0.0

"""

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as pp

# Reading the csv file
tb_dataset = pd.read_csv('tb.csv', encoding= 'latin-1')
sex = ['f','m','f','m','f']

# Reading the country AD with year 1996
required_data = tb_dataset.query('country == "AD" and year==1996')

#  Finding the cases for each group of age
required_data = required_data.melt(['country', 'year'],['f1524', 'm1524', 'f2534', 'm2534', 'f3544' ],'age', 'cases')
required_data['sex'] = sex 

# Renaming the names of the age columns
required_data['age'] = required_data['age'].map({'f1524': '15-24', 'm1524':'15-24', 'f2534':'25-34', 'm2534':'25-34','f3544':'35-44' }) 


#Setting the sequence of the schema
sex = required_data.pop('sex')
cases = required_data.pop('cases')

required_data['sex'] = sex
required_data['cases'] = cases




