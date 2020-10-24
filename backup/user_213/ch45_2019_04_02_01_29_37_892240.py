def zera_negativos(num):
    i=0
    while i<len(num):
        i+=1
        while num[i]<0:
            num[i]=0
    return num
    
    
    