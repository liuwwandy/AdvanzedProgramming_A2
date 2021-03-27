# -*- coding: utf-8 -*-
"""
"""

import pandas as pd
import copy
from functools import reduce
from collections import defaultdict

cars = pd.read_csv('auto-mpg.data', delim_whitespace=True,header=None)
cars.describe()
# The response variable is mpg (miles per gallon)
# Attribute 6 is the car model year: 70, 71, 72, ..., 82
modelyear = cars.iloc[:,6].tolist()
mpg = cars.iloc[:,0].tolist() 

#Step 2: Creation of a default dictionary which use as initial value an empty list
 
dd = defaultdict(lambda:list())
#For each of the values in the modelyear, append the value of mpg with the same 
#index in the list which key is the modelyear 
for index in range(0,len(mpg)):
    dd[modelyear[index]].append(mpg[index])

#Step 3:for each of the keys and values in dd, replace the value of the list by
#the sum of all the values of the list by the number of elements.   
    
for k,value in dd.items():
    dd[k]= reduce(lambda x,y:x+y,value)/len(value)

#Step 4: Create a copy of modelyear and in that list use list comprehension to 
# replace the value of the list for the value in the dictionary dd which key 
# is the value of modelyear
    
modelyear_cat = copy.deepcopy(modelyear)
modelyear_cat = [dd[a] for a in modelyear_cat]

#Save the file in order to be able to hand it in.
out_file = open('result.txt', 'w')
for value in modelyear_cat:
    out_file.write(str(value) + '\n')
out_file.close()
