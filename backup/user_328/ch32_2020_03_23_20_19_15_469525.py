def eh_primos (a):
    if x==1 or x==0 :
        return (False)
    if x==2:
        return (True)
    if x%2==0:
        return (False)
    a=3
    while a<x:
        if x%a==0:
            return (False)
        a= a + 1
    return (True) 
def lista_primos (quantidade) :
    contador = 1
    numero = 1
    lista = []
    while contador <= quantidade:
        if eh_primos(x):
            lista.append(x)
            contador += 1
        x += 1
    return lista



    