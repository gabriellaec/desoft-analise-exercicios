lista = [1]*10
i=0
s=[0]*10
x=len(lista)
def soma_valores (i):
    while i<x:
        s[i+1] = s[i] + lista[i]
        i=i+1
    return s[i+1]