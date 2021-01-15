#lwm_sandbox.py

#needed libraries
#~ import os
#~ import sys
#~ import datetime
#~ import shutil
#~ import subprocess
import pandas as pd
import numpy as np

#Read in the file

#variables for importing csv to dataframe
file = '2019-12-12-00_example_LWM.csv'
fields = ['measure', 'code']

#only impport the columns we want to df, the dataframe, use them all
df = pd.read_csv(file, usecols=fields)

print('Original dataframe import:')
print(df)

#This gets the job done
#BRUTE FORCE WINS
mouth = df.loc[df.code=='mouth', 'measure'].values[0]        #get the row index where code = 'mouth' and use index to get value in 'measure' assign to variable mouth
head = df.loc[df.code=='head', 'measure'].values[0]
run = df.loc[df.code=='run', 'measure'].values[0]

print('brute force wins!')
print(mouth)
print(head)
print(run)
print('brute force suckers!!!')


#set variables with a list and a loop
variables = ['mouth', 'head', 'run']
#~ print(variables[0])
#~ print(variables[1])
#~ print(variables[2])
print('################')
for x in variables:
	(variables[x]) = (df.loc[df.code==x, 'measure'].values[0]) #how to get a function to set a variable name?

#output to verify success
print(mouth)
print(head)
print(run)
print('yeah, the loop worked?')
