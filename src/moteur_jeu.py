
# Création de notre grille de jeu contenant 6 lignes et 7 colonnes
def creation_grille(m: int= 6, n: int= 7): 
    grille = [[0]*n for i in range(m)] 
    return grille

# Fonction permettant d'afficher notre grille de jeu
def afficher_grille(grille:list):   
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            print(grille[i][j], end='  ')
        print()

#Fonction permettant l'insertion des pions dans la grille
def insertion_pion(pion_inserer:int, grille:list):
    coup_joué = 1
    index = len(grille)-(len(grille)+1)
    while(coup_joué==1):
        if(index==-7):
            print("Cette colonne est deja pleine. Choisissez en une autre")
            index = len(grille)-(len(grille)+1)

        while True:
            try:
                colonne = int(input("Veillez choisir dans quelle colonne vous allez insérer votre pion "))
                break
            except ValueError:
                print("Vous n'avez pas entré une valeur entiere, veillez réessayer")
                print()
                
        while(colonne<0 or colonne>6 or type(colonne)!=int): #Vérification de la colonne entrée par l'utilisateur
            print ("Vous avez entré un choix invalide")
            print("Veillez choisir un numéro de colonne entre 0 et 6")
            colonne = int(input("Veillez choisir dans quelle colonne vous allez insérer votre pion "))

        #Insertion du pion dans la colonne choisi 
        parcour = 1 #Variable permettant de parcourir la liste du bas vers le haut en soustrayant cette valeur à n pour avoir des indices négatifs décroissant
        while(index>-7):
            if(grille[index][colonne] == 0):
                grille[index][colonne] = pion_inserer
                coup_joué=0
                break
            else:
                index -= 1
        
    return [grille,colonne] #Nous retournons egalement la colonne joué pour pouvoir utiliser cette information dans l'entrainement du modèle

#Vérification d'une combinaison gagnante dans la grille
def verification_gagnant(grille:list, joueur:int):
    state_vict=0
    for m in range(len(grille)):
        for n in range(len(grille[m])):
            dx=1
            dy=1
            compteur = 1
            if(grille[m][n]!=0):
                # Recherche d'un pion correspondant dans la direction horizontale vers la droite
                if(m<3): # Avant de chercher une ligne gagnante, on vérifie si on ne risque pas sortir de notre grille. Si faire la vérification implique sortir de la 
                    #grille alors ca veut juste dire que nous ne sommes pas dans une position où l'on peut avoir une potentielle victoire
                    while(grille[m+dx][n]==grille[m][n]):
                        compteur+=1
                        dx+=1
                        if(compteur==4):
                            print(f"Nous avons une combinaison gagnante verticale pour le joueur {joueur}")
                            state_vict=1
                            break
                    dx=1;compteur = 1                    

                # Recherche d'un pion correspondant dans la direction verticale vers le bas
                if(n<4): # On vérifie s'il y a assez de case en bas pour pouvoir procéder à la vérification
                    while(grille[m][n+dy]==grille[m][n]):
                        compteur+=1
                        dy+=1
                        if(compteur==4):
                            print(f"Nous avons une combinaison gagnante horizontale pour le joueur {joueur}")
                            state_vict=1
                            break
                    dy=1;compteur = 1
                    
                #Recherche d'un pion sur la diagonnale bas-droit
                if(m<3 and n<4): # On vérifie s'il y a assez de case dans la diagonale pour pouvoir effectuer la vérification
                    while(grille[m+dx][n+dy]==grille[m][n]):
                        compteur+=1
                        dx+=1
                        dy+=1
                        if(compteur==4):
                            print(f"Nous avons une combinaison gagnante oblique droite haute pour le joueur {joueur}")
                            state_vict=1
                            break
                    dx=1;dy=1;compteur = 1

                #Recherche d'un pion sur la diagonale bas-gauche
                if(m<3 and n>2): # On vérifie s'il y a assez de case dans la diagonale pour pouvoir effectuer la vérification
                    while(grille[m+dx][n-dy]==grille[m][n]):
                        compteur+=1
                        dx+=1
                        dy+=1
                        if(compteur==4):
                            print(f"Nous avons une combinaison gagnante oblique gauche basse pour le joueur {joueur}")
                            state_vict=1
                            break
                    dx=1;dy=1;compteur = 1

    return state_vict



#grille_test = [[0,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,0,0]]
#afficher_grille(grille_test)
#verification_gagnant(grille_test,1)






#grille = creation_grille()
#grille = insertion_pion(1,grille)
#afficher_grille(grille)
