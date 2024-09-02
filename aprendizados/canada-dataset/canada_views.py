# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:56:32 2024

@author: yandrade
"""
import plotly.express as px
import pandas as pd

steps = pd.DataFrame([[112,34], [22, 572], [142, 671], [739, 41]], 
                     index=['seg', 'ter', 'qua', 'qui'],
                     columns=['A', 'B'])

fig = px.bar(steps, x='A', y='B')

fig.show()