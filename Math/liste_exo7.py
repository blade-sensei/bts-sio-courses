nombre = [3,50,20,7,14,2,9,16]
taille = len(nombre)

for i in  range(taille):
    if i==taille-1:
        nombre[i]=nombre[0]
print(nombre)
