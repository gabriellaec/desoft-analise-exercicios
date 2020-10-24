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

def verifica_primos(lista):
    saida = {}
    for e in lista:
        if primos(e) == True:
            saida[e] = True
        elif primos(e) == False:
            saida[e] = False
    return saida

