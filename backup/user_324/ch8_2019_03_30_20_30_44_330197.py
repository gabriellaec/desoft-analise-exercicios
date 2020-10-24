
def verifica_progressao(x,y, z, o):
    i=0
    a=int(lista[i])
    b=int(lista[i+1])
    c=int(lista[i+2])
    for e in lista:
        if b-a==c-b:
            return A
        elif b/a==c/b:
            return G
        elif b-a==c-b and b/a==c/b:
            return AG
        elif b-a!=c-a and b/a!=c/b:
            return NA
        i+=2
A="P.A"
G="P.G"
AG="A.G"
NA='N/A'
print(verifica_progressao(A,G, AG, NA))