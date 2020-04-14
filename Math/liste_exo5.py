nombre = [3,50,20,7,14,2,9,16]
taille = len(nombre)
pair =[]
impair =[]
for i in  range(taille):
    if nombre[i]%2 == 0:
        pair.append(nombre[i])
    else:
        impair.append(nombre[i])
print(pair)
print(impair)
