def eh_crescente(x):
    x=[]
    i=0
    while i<len(x):
        if x[i]<x[i+1]:
            return True
            i+=1
        else: 
            return False