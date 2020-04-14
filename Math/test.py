t1=[31,28,31,30,31,30,31,30,31,30,31]
t2=['janvier','fevrier','mars','avril','mai','juin','juillet','aout','septembre','octrobre',
    'novembre','decembre']
t3=[]
txt = ""
jours=len(t1)
mois=len(t2)

for i in range (len(t2)):
    txt += t2[i]

print(txt)

