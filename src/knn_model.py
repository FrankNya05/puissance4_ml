import pandas as pd
import numpy as np
from joblib import dump
from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split 
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import validation_curve
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import learning_curve

donnee = pd.read_csv('data/resultats.csv')
print(donnee.head())
data= donnee.drop('target',axis=1)


def data_processing(data:pd.DataFrame):

    col_modif= data.columns[data.columns != 'joueur']

    mask_joueur1 = data['joueur']== 1
    mask_case_value_joueur1 = data[col_modif] == 2 #Masque booleen indexant toutes les cases du dataframe étant egal à 2
    data.loc[mask_joueur1, col_modif] = data.loc[mask_joueur1, col_modif].mask(mask_case_value_joueur1.loc[mask_joueur1], -1) #Au tour du joueur 1, on remplace les 2 par des -1


    mask_joueur2 = data['joueur']== 2 # Boolean mask permettant d'indexer les cases de la colonne joueur etant egale a 2

    mask_case_value1 = data[col_modif] == 1 #Masque booleen indexant toutes les cases du dataframe étant egal à 2

    # Ici, on s'en va dans les colonnes à modifier à la recherche de celle correspondant au tour du joueur 2 et qui ont les valeur 1 qu'on remplacera par -1. De cette maniere, le modèle recevra des 
    # données symetriques. Au tour du joueur 2 celui ci jouera le role 1 contre -1 l'adversaire. Ce qui sera egalement pareil au tour du joueur 1
    data.loc[mask_joueur2, col_modif] = data.loc[mask_joueur2, col_modif].mask(mask_case_value1.loc[mask_joueur2], -1)


    mask_case_value2 = data[col_modif] == 2 #Masque booleen indexant toutes les cases du dataframe étant egal à 2
    #Ici, au tour du joueur 2, on remplace les 2 par des 1
    data.loc[mask_joueur2, col_modif] = data.loc[mask_joueur2, col_modif].mask(mask_case_value2.loc[mask_joueur2], 1)

    return data



#condition_modif_1= (data['joueur']==2) & (data.loc[:,col_modif.to_list()]==1)
#condition_modif_2= (data['joueur']==2) & (data.loc[:,col_modif.to_list()]==2)
#print(condition_modif_1.head())
#print(type(condition_modif_1))

#for i in condition_modif_1.index:
#    data.loc[i,col_modif.to_list()]=-1

#for j in condition_modif_2.index:
#    data.loc[j,col_modif.to_list()]=1


#data.loc[condition_modif_1,col_modif.to_list()]=-1
#data.loc[condition_modif_2,col_modif.to_list()]=1


train_data = data_processing(data)

# La variable x correspond à un dataframe contenant toutes les colonnes case. Et la variable y correspond à la colonne target, la colonne joueur n'est pas utilisé pour ce modele
y= donnee['target']
x = train_data.drop('joueur', axis=1)
x_train, x_test, y_train, y_test= train_test_split(x,y, test_size=0.2, random_state= 6)

parametre = {'n_neighbors': np.arange(1,50,1),
              'weights':['uniform', 'distance'],
              'metric': ['euclidean','manhattan','cosine','minkowski']}

grid = GridSearchCV(KNeighborsClassifier(),param_grid=parametre,n_jobs=8,cv=5)
grid.fit(x_train,y_train)

print(f'Le meilleur score est {grid.best_score_}')
print(f'Les meilleurs paramètres sont: {grid.best_params_}')

model= grid.best_estimator_
print(model.score(x_test,y_test))

