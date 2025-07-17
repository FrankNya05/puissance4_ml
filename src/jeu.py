from moteur_jeu import*

#Initialisation de la grille de jeu
grille = creation_grille()
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
    grille = insertion_pion(joueur,grille)
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
    grille = insertion_pion(joueur,grille)
    afficher_grille(grille)
    etat_joueur2=verification_gagnant(grille,joueur)
    
    if(etat_joueur2==1):
        print("FÉLICITATIONS !!!")
        print()
        print("Le joueur 2 à remporter la partie")
        partie=0
        break
