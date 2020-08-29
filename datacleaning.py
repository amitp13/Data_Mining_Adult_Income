#Data Cleaning


#import libraries
import pandas as pd
import numpy as np

#read data
df = pd.read_csv("adult.csv")

#parsing gender
df['sex'].replace(['Male','Female'],['M','F'], inplace=True)


#parsing martial status
def marital_status(x):
    if x == 'Married-civ-spouse' or x == 'Married-spouse-absent' or x == 'Married-AF-spouse':
        return 'Married'
    else:
        return 'Single'

df['status'] = df['marital.status'].apply(lambda x: marital_status(x))


#parsing education
def education(x):
    if x == 'Bachelors' or x == 'Some-college':
        return 'Bachelors'
    elif x == 'Assoc-voc' or x== 'Assoc-acdm':
        return 'Associate'
    elif x == '1st-4th' or x == '1st-4th' or x == '7th-8th' or x == '9th' or x == '10th' or x == '11th' or x == '12th' or x == 'HS-grad':
        return 'High School'
    else:
        return x

df['education'] = df['education'].apply(lambda x: education(x))


#handling null values 
for i in df.columns:
    df[i].replace('?', np.nan, inplace=True)

print(df.isnull().sum())

x = df.shape
print('Shape: {}'.format(x))

df = df.dropna(subset=['workclass','occupation','native.country'], how='all')

y = df.shape
print("Rows Dropped: {}".format(x[0] - y[0]))
print("Shape: {}".format(y))


df.head()

