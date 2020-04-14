from random import*
#-----Exo1 Composer se matrice
def matrice(n,m):
    mat=[]
    for i in range(0,m):
        ligne=[]
        for j in range(0,m):
            print("ligne",i+1,"colonne",j+1)
            val=input("Entrez")
            ligne.append(val)
        mat.append(ligne)
    return mat
#-----Exo1 Composer sa matrice

def matriceB(n,m):
    M=[[0 for j in range(n)]for i in range(n)]
    for i in range(0,m):
        for j in range(0,m):
            print("Modifier")
            M[i][j]=int(input("nombre"))
    return M

#-----Exo2 Matrice Carré de 0
def matnulle(n,p):
    mat=[]
    for i in range(0,n):
        ligne=[]
        for j in range(0,p):
            valeur_nulle=0
            ligne.append(valeur_nulle)
        mat.append(ligne)
    return mat

#-----Exo3 Matrice carré diagonale 1

def matident(n):
    mat=matnulle(n,n)
    for i in range(0,n):
        mat[i][i]=1
    return mat
        

#-----Exo4 Matrice alétoire 

def matalea(n,p): 
    mat=[]
    for i in range(0,p):
        ligne=[]
        for j in range(0,n):
            val = randint(1,9)
            ligne.append(val)
        mat.append(ligne)
    return mat
#------Exo5 Addition des matrice

def somme(mat1,mat2):
    res=0
    valide = True
    if (len(mat1) == len(mat2)):# nombre de lignes
        if(len(mat1[0]) == len(mat2[0])): #nombre de colonnes de ligne 0
            valide = True
        else:
            valide = False
    else:
        valide = False

    if (valide == True):
        print("ok")
        resultat=matnulle(len(mat1),len(mat1[0]))
        for l in range(0,len(mat1)):
            for c in range(0,len(mat1[0])):
                resultat[l][c] = mat1[l][c]+mat2[l][c]
        return resultat
                
    else:
        print("erreur de taille matrice")

#-----Exo6 Prodreel Multiplication par un nombre k
def prodreel(mat1,k):
    res=0
    valide = True
    resultat=matnulle(len(mat1),len(mat1[0]))
    for l in range(0,len(mat1)):
        for c in range(0,len(mat1[0])):
            resultat[l][c] = mat1[l][c]*k
    return resultat
   
#------Exo9
    



    

   
    

