# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:56:32 2024

@author: yandrade
"""
import plotly.express as px
import pandas as pd

df = pd.read_csv('canada.csv')

px.line(
    df,
    x='Country of Citizenship',
    y='2015'
)

px.show()
