def eh_primo(x): 
    if x<=1:
        return (False)
    if x==2:
        return (True)
    if x%2==0:
        return (False)
    a= 3
    while a<x:
        if x%a==0:
            return (False)
        else:
            a+=2
    return (True)


def lista_primos(n):
    lista=[0]*n
    indice=0
    numero=2
    while indice<n:
        if eh_primo(numero)==True:
            lista[indice]=numero
            indice+=1
        numero+=1
    return (lista)
    