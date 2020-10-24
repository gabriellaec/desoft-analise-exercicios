def verifica_primos(lista):
    dicionario = {}
    for e in lista:
        while e >1:
            if e%1 ==0 and e%e==0:
                dicionario["True"]="e"
            else:
                dicionario["False"]="e"
    return dicionario
            