#COYLA SIOA1


choixtriangle = input("Entrer 1, 2 ou 3 pour obtenir un motif: ")
choixligne = int(input("Choisissez le nombre de lignes: "))
ch = "" 
etoile = ""
ligne = choixligne
nbretoile = 1



if choixtriangle == "1":
        for i in range(choixligne):
            for i in range(ligne):
                etoile = etoile + "*"
            print(etoile)
            ligne = ligne-1
            etoile = ""

elif choixtriangle == "2":
    for i in range(choixligne):
        ch = "*" + ch
        print(ch)

elif choixtriangle == "3":
            for i in range(choixligne):
                for i in range(choixligne):
                    etoile=etoile+" "
                for i in range(nbretoile):
                    etoile=etoile+"*"
                print(etoile)
                etoile = ""
                nbretoile=nbretoile+2
                choixligne = choixligne-1

