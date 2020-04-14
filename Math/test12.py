
def nbre_premier(n):
    crible=list(range(2,n+1))
    k=2
    while k<=(len(crible)):
        for l in range (k,n):  # peut etre pas n
            i=crible[l]
            if i!=k:
                reste=i%k

                if reste==0:
                    crible.remove(i)
        k=k+1
                    
    return crible
    
