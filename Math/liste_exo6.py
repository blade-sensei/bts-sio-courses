maliste=["Jean","Maximiilien","Brigitte","Sonia","Jean-Pierre","Sandra"]
moins=[]
plus=[]
taille=len(maliste)

for i in range(taille):
    if len(maliste[i]) < 6:
         moins.append(maliste[i])
    else:
        plus.append(maliste[i])
print(moins)
print(plus)
