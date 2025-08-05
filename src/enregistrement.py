import csv
import os

# Aplatissement de notre grille pour avoir une liste plate que le modèle de machine learning pourra comprendre
def aplatissement_grille(liste: list):
    liste_plat = [element for sublist in liste for element in sublist]
    return liste_plat

#Création d'une nouvelle liste qui contiendra notre grille aplatie, le joueur ayant joué et la case que ce dernier aura joué
#C'est grille qui sera passé plustard dans notre modèle pour l'apprentissage
def grille_formate(liste_plat: list, joueur_courant: int, target: int):
    liste_plat.append(joueur_courant)
    liste_plat.append(target)
    liste_formate = liste_plat
    return liste_formate

#Cette fonction permet de recuperer le chemin du repertoire data dans lequel nous ferons la sauvegarde de nos données sous forme de fichier csv
def recuperation_path():
    file_path = os.path.abspath(__file__)
    repertoire = os.path.dirname(file_path)
    projet_path = os.path.dirname(repertoire)
    data_path = os.path.join(projet_path, 'data')
    save_file = os.path.join(data_path, 'resultats.csv')
    return save_file

#Initialisation de notre fichier avec une première ligne contenant le nom de chaque colonne
def initialisation_fichier(liste_formate: list, chemin_fichier: str):
    if not os.path.exists(chemin_fichier) or os.path.getsize(chemin_fichier) == 0:
        with open(f'{chemin_fichier}','a',newline='') as data_csv:
            newline= csv.writer(data_csv)
            premiere_ligne = [f'case{i+1}' for i in range(len(liste_formate))]
            premiere_ligne.append('joueur')
            premiere_ligne.append('target')
            newline.writerow(premiere_ligne)

#Sauvegarde de la nouvelle liste formatée contenant l'etat de la grille et le joueur qui va jouer ainsi que le coup qu'il jouera
def sauvegarde(liste_formate: list, chemin_fichier : str):
    with open(f'{chemin_fichier}', 'a', newline='') as data_csv:
        newline = csv.writer(data_csv)
        newline.writerow(liste_formate)

grille_test = [[0,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,0,0]]
recuperation_path()
grille_plat = aplatissement_grille(grille_test)
print (grille_plat)
