def Premiers (n):
    k=2;
    crible=[]
    crible=list(range(2,n))
    for i in crible:
        for k in crible:
            if i%k==0 and i!=k:
                crible.remove(k)
        k=k+1
    print(crible)
    print(k)
