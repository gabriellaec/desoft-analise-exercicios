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

def verifica_primos(lista1):
    dict = {}
    for i in lista1:
        dict[i] = eh_primo(i)
    return dict