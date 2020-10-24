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

indice=0
numero=2
def lista_primos(n):
    lista_primos=[0]*n
while indice<n:
    if eh_primo(numero)=True:
        lista[indice]=numero
        indice+=1
    numero+=1
return (lista_primos)
    