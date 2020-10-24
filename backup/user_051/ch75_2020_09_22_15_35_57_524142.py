def verifica_primos(lista):
    i=0
    lista_1=[]
    while i < len(lista):
        primo=eh_primo(lista[i])
        lista_1.append(primo)
        i+=1
    dicionario=dict(zip(lista, lista_1))
    return dicionario

def eh_primo(X):
    if X<0:
        return False
    if X==0 or X==1:
        return False
    if X==2:
        return True
    if X%2==0:
        return False
    Z=3
    while Z<X:
        if X%Z==0:
            return False
        Z+=2
    return True
lista = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
q=verifica_primos(lista)
print (q)