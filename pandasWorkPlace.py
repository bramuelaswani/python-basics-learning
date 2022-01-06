# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 14:05:03 2021

@author: User
"""

import pandas as pd
#creating data frames
'''fruits=pd.DataFrame([[30,21]], columns=["apples", "Bananas"])
print(fruits)'''

'''fruit_sales=([[35,21],[4,54]], columns=['apples','bananas'],
             index=['2012 sales','2013 sakes'])'''

quantities=['4 cups','1 cup', '2large', "1 can"]
items=['flour','milk','eggs','spam']
recipe=pd.Series(quantities,index=items,name='Dinner')
print(recipe)

#reading dataframes
df=pd.read_csv("path")

#Writting
#animals.to_csv("path.csv")
