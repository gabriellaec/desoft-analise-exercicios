def zera_negativos(num):
    i=0
    while i<len(num):
        i+=1
        if num[i]<0:
            num[i]=0
        else:
            num[i]=num[i]
    return num
    
    
    