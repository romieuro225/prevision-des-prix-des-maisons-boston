# -*- coding: utf-8 -*-
"""Prevision_prix_maisons_boston.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aXCJ0OkVLUHG-uhV2AiuMY0GmkqM2-NC
"""

#Importer les bibliothèques
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split

#Importer le base de données boston house
from sklearn.datasets import load_boston
boston=load_boston()
boston.keys()

boston.feature_names

boston.target

#Préparation de la base de données 
df_x=pd.DataFrame(boston.data, columns=boston.feature_names)
df_y=pd.DataFrame(boston.target)
print(df_x.head())
print(df_y.head())

#Création du modèle
reg=linear_model.LinearRegression()

#Préparer la base de données d'entrainement
x_train,x_test, y_train, y_test=train_test_split(df_x,df_y, test_size=0.2,random_state=42)

print(x_train.shape)
print(x_test.shape)

#Entrainement du modèle
reg.fit(x_train,y_train)

#Faire des prévisions en utilisant le modèle
y_pred=reg.predict(x_test)
print(y_pred)

print(y_test)

#Calculer la performance du modèle en utilisant MSE
print(np.mean(y_test-y_pred)**2)

from sklearn.metrics import mean_squared_error
print(mean_squared_error(y_test,y_pred))