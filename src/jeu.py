from moteur_jeu import*
from enregistrement import*
from joblib import load

#Initialisation de la grille de jeu et du fichier de sauvegarde

grille = creation_grille() #creation de la grille de jeu
grille_plat= aplatissement_grille(grille) #Aplatissement de la grille 
data_path= recuperation_path() #Récuperation du chemin d'accès vers le repertoire data
initialisation_fichier(grille_plat,data_path) #Initialisation du fichier csv

#Chargement du modele de machine learning
DecisionTre= load('DecisionTreep4.joblib')

print("B.I.E.V.E.N.U.E DANS CETTE NOUVELLE PARTIE DE PUISSANCE 4")
print()
print("Amusez vous bien:)")
print()
print("La partie débutera par le joueur 1 qui aura les pions rouges")
print()
afficher_grille(grille)

#Démarrage de la partie
partie = 1
etat_joueur1 =0
etat_joueur2 =0

while(partie==1):

    joueur = 1
    print(f"JOUEUR {joueur} à vous de jouer")
    grille_plat= aplatissement_grille(grille) #Aplatissement de la grille pour le joueur 1
    grille,coup_joue = insertion_pion(joueur,grille)
    
    #Sauvegarde de la grille et du coup joué par le joueur 1
    liste_formate= grille_formate(grille_plat,joueur,coup_joue)
    sauvegarde(liste_formate,data_path)

    afficher_grille(grille)
    etat_joueur1=verification_gagnant(grille,joueur)

    if(etat_joueur1==1):
        print("FÉLICITATIONS !!!")
        print()
        print("Le joueur 1 à remporter la partie")
        partie=0
        break
        
    joueur = 2
    print(f"JOUEUR {joueur} à vous de jouer")
    grille_plat= aplatissement_grille(grille) #Aplatissement de la grille pour le joueur2 au debut de son tour de jeu
    grille,coup_joue = insertion_pion(joueur,grille)

    #Sauvegarde de la grille et du coup joué par le joueur 2
    liste_formate= grille_formate(grille_plat,joueur,coup_joue)
    sauvegarde(liste_formate,data_path)

    afficher_grille(grille)
    etat_joueur2=verification_gagnant(grille,joueur)
    
    if(etat_joueur2==1):
        print("FÉLICITATIONS !!!")
        print()
        print("Le joueur 2 à remporter la partie")
        partie=0
        break
