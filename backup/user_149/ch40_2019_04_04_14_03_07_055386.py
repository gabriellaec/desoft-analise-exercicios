def fatorial(x):
    
    numeros=[]
    i=1
    s=0
    while i<=x:
        numeros.append(i)
        i+=1
    while s<len(numeros):
        numeros[s]=numeros[s]*numeros[s-1]
        s+=1

    
    return numeros[-2]