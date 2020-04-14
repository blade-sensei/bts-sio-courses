t1=[31,28,31,30,31,30,31,31,30,31,30,31]
t2=["Janvier","Fevrier","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre",
    "Octobre","Novembre","Decembre"]
jour=len(t1)
mois=len(t2)
t3=[]
for i in range(jour):
    t3.append(t2[i])
    t3.append(t1[i])
    
print(t3)
