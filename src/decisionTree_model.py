import pandas as pd
import numpy as np
from joblib import dump
from matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split 
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import validation_curve
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import learning_curve

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

donnee = pd.read_csv('data/resultats.csv')

# La variable x correspond à un dataframe contenant toutes les colonnes case. Et la variable y correspond à la colonne target, la colonne joueur n'est pas utilisé pour ce modele
y= donnee['target']
#x= donnee.drop('target', axis=1)
x = data_processing(donnee.drop('target', axis=1)).drop('joueur', axis=1)
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size=0.2, random_state= 6)

# Grille d'hyperparamètres à tester
param_grid = {
    'max_depth': [3, 5, 10, None],  # Profondeur maximale de l'arbre
    'min_samples_split': [2, 5, 10],  # Min d’échantillons pour faire une division
    'min_samples_leaf': [1, 2, 4],    # Min d’échantillons dans une feuille
    'criterion': ['gini', 'entropy'], # Fonction de décision (gini = par défaut)
}

# Recherche des meilleurs hyperparametres pour le modele de DecisionTree
grid_search = GridSearchCV(estimator=DecisionTreeClassifier(random_state=5), param_grid=param_grid, scoring='accuracy', cv=5, n_jobs=-1, verbose=1)
grid_search.fit(x_train,y_train)
print('Le meilleur score est ',grid_search.best_score_)
print('Les meilleurs parametres sont', grid_search.best_params_)

model= grid_search.best_estimator_
print('Les resultats de test sont', model.score(x_test,y_test))

#Sauvegarde du modele et de ces hyperparametres dans un fichier
dump(model,'DecisionTreep4.joblib')

#model.fit(x_train,y_train)
#print(model.score(x_test,y_test))