# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:05:19 2019

@author: PAVI
"""

import pandas as pd
import numpy as np

# Read the three csv files which contains the score of same students in term1 for each Subject

ds_data = pd.read_csv(r'DSScoreTerm1.csv',delimiter=',')
print(ds_data)

maths_data = pd.read_csv(r'MathScoreTerm1.csv',delimiter=',')
print(maths_data)

physics_data = pd.read_csv(r'PhysicsScoreTerm1.csv',delimiter=',')
print(physics_data)

ds_data.info()
maths_data.info()
physics_data.info()

# Remove the name and ethnicity column (to ensure confidentiality)

ds_data.drop(['Name','Ethinicity'],inplace=True,axis=1)
maths_data.drop(['Name','Ethinicity'],inplace=True,axis=1)
physics_data.drop(['Name','Ethinicity'],inplace=True,axis=1)

# Fill missing score data with zero

ds_data.Score.isna().value_counts()
maths_data.Score.isna().value_counts()
physics_data.Score.isna().value_counts()

ds_data['Score']=ds_data['Score'].fillna(0)
maths_data['Score'] = maths_data['Score'].fillna(0)
physics_data['Score']=physics_data['Score'].fillna(0)

ds_data.Score.isna().value_counts()
maths_data.Score.isna().value_counts()
physics_data.Score.isna().value_counts()

# Merge the three files

merge1 = pd.merge(ds_data,maths_data,how='inner',on='ID')
merge1.rename(columns={'Score_x':'Ds_Score', 'Age_x':'Age' , 'Sex_x':'Sex', 'Score_y':'Maths_Score'},
              inplace=True)

merge1.drop(['Subject_x','Subject_y','Age_y','Sex_y'],inplace=True,axis=1)

merge2 = pd.merge(merge1,physics_data,how='inner',on='ID')
merge2.rename(columns={'Score':'Physics_Score', 'Age_x':'Age' , 'Sex_x':'Sex'},
              inplace=True)

merge2.drop(['Age_y','Sex_y','Subject'],inplace=True,axis=1)

merged_data = pd.DataFrame(merge2)

# Change Sex(M/F) Column to 1/2 for further analysis

merged_data['Sex']=merged_data['Sex'].apply(lambda x: 1 if x=='M' else 2) 
merged_data.info()

# Store the data in new file – ScoreFinal.csv

merged_data.to_csv(r'C:\Users\PAVI\Desktop\Edureka\Python Certification\Module4\ScoreFinal.csv',index=False)

# Enhancements for code
# Convert ethnicity to numerical value

ds1_data = pd.read_csv(r'DSScoreTerm1.csv',delimiter=',')
print(ds_data)

maths1_data = pd.read_csv(r'MathScoreTerm1.csv',delimiter=',')
print(maths_data)

physics1_data = pd.read_csv(r'PhysicsScoreTerm1.csv',delimiter=',')
print(physics_data)

ds1_data.info()
maths1_data.info()
physics1_data.info()

ds1_data['Ethinicity']=ds1_data['Ethinicity'].apply(lambda x: 1 if x=='African American' else ( 2 if x=='European American' else ( 3 if x=='White American' else 4)))
maths1_data['Ethinicity']=maths1_data['Ethinicity'].apply(lambda x: 1 if x=='African American' else ( 2 if x=='European American' else ( 3 if x=='White American' else 4)))
physics1_data['Ethinicity']=physics1_data['Ethinicity'].apply(lambda x: 1 if x=='African American' else ( 2 if x=='European American' else ( 3 if x=='White American' else 4)))

ds1_data.info()
maths1_data.info()
physics1_data.info()

# Fill the missing score for a student to the average of the class

ds1_data.Score.isna().value_counts()
maths1_data.Score.isna().value_counts()
physics1_data.Score.isna().value_counts()

ds1_data['Score']=ds1_data['Score'].fillna(ds1_data.mean()['Score'])
maths1_data['Score'] = maths1_data['Score'].fillna(maths1_data.mean()['Score'])
physics1_data['Score']=physics1_data['Score'].fillna(physics1_data.mean()['Score'])

ds1_data.Score.isna().value_counts()
maths1_data.Score.isna().value_counts()
physics1_data.Score.isna().value_counts()

