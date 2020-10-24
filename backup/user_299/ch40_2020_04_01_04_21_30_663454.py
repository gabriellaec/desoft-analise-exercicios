lista = [1]*10
i=0
s=0
x=len(lista)
def soma_valores (lista,i,s):
    while i<x:
        s = s + lista[i]
        i=i+1
    return s