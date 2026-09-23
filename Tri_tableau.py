#Ce programme construit un tableau d'une seule ligne et plusieurs colonnes, l'affiche, le trie puis le réaffiche
def construit_tableau(nombre_colonnes):
    import random
    tableau = []
    for i in range(nombre_colonnes):
        valeur = random.randint(1,100)
        tableau.append(valeur)
    return tableau

def affiche_tableau(tableau):
    print("-"*len(tableau)*5 , end='') 
    print("\n", end='')
    for valeur in tableau:
        print("! " + str(valeur), end=' ')
    print(" !\n", end='')
    print("-"*len(tableau)*5 , end='') 
    print()

def tri_tableau(tableau):
    for i in range(len(tableau)):
        for j in range(i+1, len(tableau)):
            if tableau[i] > tableau[j]:
                tableau[i], tableau[j] = tableau[j], tableau[i]
    return tableau

def affichage():
    global tableau
    tableau[2] = 100
    tableau =tableau + [200, 300]
    print("tableau [1]:", tableau[1])
    print("tableau [-1]:", tableau[-1])
    print("tableau [2:5]:", tableau[2:5])
    
    del tableau[4]
    tableau.insert(4, 400)
    tableau.append(400)
    print("tableau [:]:", tableau[:])
    tableau.remove(400)
    tableau.sort(reverse=True)
    print("tableau [0:]:", tableau[0:])
    print("longueur tableau [:]:", len(tableau))
    if 1000 in tableau:
        print("1000 est dans le tableau")
    else:
        print("1000 n'est pas dans le tableau")

  

tableau = construit_tableau(10)
affiche_tableau(tableau)
tri_tableau(tableau)
affiche_tableau(tableau)
tableau = [78, 45, 23, 56, 12, 89, 34, 67, 90, 11]
affiche_tableau(tableau)
tri_tableau(tableau)
affiche_tableau(tableau)
affichage()