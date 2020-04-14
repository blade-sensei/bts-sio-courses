#Compter les elements non nuls
nombre = [3,50,20,7,14,2,9,16]
taille = len(nombre)
elements = 0;
resultat = 0;
place = 0;

for i in range(taille):
    if nombre[i] == 0:
        elements = elements+1
resultat = taille - elements
print(resultat)

#Trouver le maximum de la liste
maximum = max(nombre)
print(maximum)

#Trouver la place du minimum de la liste
minimum = min(nombre)
for i in range(taille):
    if nombre[i] == minimum:
        place = i
print(place)

#Mim et max sans max() min()
mini = nombre[0]
maxi = nombre[0]
for i in range(taille):
    if nombre[i] > maxi:
        maxi = nombre[i]
    if nombre[i] < mini:
        mini = nombre[i]
print(maxi)
print(mini)
