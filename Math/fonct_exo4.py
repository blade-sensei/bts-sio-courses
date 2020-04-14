def premier(n):
    prem=True
    for i in range(2,n):
        reste=n%i
        if reste==0:
            prem=False
    return prem


        
