#COYLA
def Premiers (n): 
    premiers = [2] #la liste contient 2#
    for i in range(3,n, 2): #On ajouter les multiples de 2 dans la liste
        premiers.append(i)
    for i in premiers:
        for p in premiers: #on parcours tout les elements de premiers
            if p % i == 0 and i != p: #On evite 2%2 3%3 5%5 car on veut 2,3,5 etc
                premiers.remove(p) #On supprime les multiples
    print(premiers)
