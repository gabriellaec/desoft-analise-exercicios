def primos(p):
    i=0
    if p==1:
        return False
    while p>0:
        for y in range(1,p+1):
            if p%y==0:
                i+=1
        if i<=2:
            return True
        else:
            return False
lista = [1,2,3,4,5,56,852,6,854,68,11,13,15,23,47]
def verifica_primos(lista):
    saida = {}
    for e in lista:
        if primos(e) == True:
            saida[e] = 1
        elif primos(e) == False:
            saida[e] = 0
    return saida
print(verifica_primos(lista))
