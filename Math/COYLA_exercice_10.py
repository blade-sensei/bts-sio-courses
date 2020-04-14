#COYLA
from math import *
nombre=6468
M=0;
i=0
p=1
r=0
M=nombre
resultat=""


while M>1:
    i=0
    p=p+1
    r=M%p
    while r==0:
        M=M//p #quotient de la division
        i=i+1
        r=M%p
    if i!=0:
            print(p,"^",i,"*")
print("=",nombre)
        

#Il faudrait mettre tout sur la meme ligne de sorte a avo
