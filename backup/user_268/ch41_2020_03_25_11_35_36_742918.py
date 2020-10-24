def zera_negativos(list):
    n=len(list)
    i=0
    while n>i:
        if list[i]<0:
            list[i]=0
        i+=1
    return list
        
    