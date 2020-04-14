#COYLA
from math import *
def Diviseur(nbr):
    div=[]
    i=1
    while i<=nbr:
        if nbr%i==0:
            div.append(i)
        i=i+1
    if len(div)==2:
        print(nbr,"est un nombre premier")
    else:
        print(div)




