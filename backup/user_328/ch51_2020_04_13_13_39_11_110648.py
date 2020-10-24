def eh_primo (x):
    if x==1 or x==0:
        return False
    if x==2:
        return True 
    if x%2 == 0:
        return False 
    a=3
    while a<x:
        if x%a==0:
            return False
        a= a + 1
    return True 

def primos_entre(a,b):
    lista1 = []
    for i in range(a,b+1):
        if eh_primo(i) == True:
            lista1.append(i)
    sorted(lista1)
    return(lista1)
