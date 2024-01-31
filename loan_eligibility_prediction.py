# -*- coding: utf-8 -*-
"""loan_eligibility_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qauPO9aanvhS3bLRJ-3CSqLgy3ElbKsJ
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
file_path = '/content/drive/MyDrive/train_u6lujuX_CVtuZ9i.csv'
loan = pd.read_csv(file_path)

loan.head(5)

len(loan)

loan.shape

loan.isnull().sum()

df=loan.dropna()

df.isnull().sum()

df.duplicated().sum()

from sklearn.preprocessing import LabelEncoder
label = LabelEncoder()

df['gender']=label.fit_transform(df['Gender'])

df.head()

df['married']=label.fit_transform(df['Married'])
df['education']=label.fit_transform(df['Education'])
df['area']=label.fit_transform(df['Property_Area'])
df['loan_status']=label.fit_transform(df['Loan_Status'])
df['loan_id']=label.fit_transform(df['Loan_ID'])
df['self_employement']=label.fit_transform(df['Self_Employed'])

df.head()

df.tail()

data=['Gender','Married','Education','Loan_Status','Property_Area','Loan_ID']
df.drop(columns=data,axis=1)

data=['Gender','Married','Education','Loan_Status','Property_Area','Loan_ID','Self_Employed']
df.drop(columns=data,axis=1)

import seaborn as sns
import matplotlib.pyplot as plt

plt.hist(df['ApplicantIncome'], bins=30, edgecolor='black')
plt.show()

sns.scatterplot(x='ApplicantIncome', y='LoanAmount', data=df)
plt.show()

sns.countplot(x='gender', hue='loan_status', data=df)
plt.title('Loan Approval by Gender')
plt.show()

