def sum(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

def verifica_progressao(lista):
    cont = 0
    if lista[0] == 0:
        for i in lista:
            if i != 0:
                cont += 1
    if cont == 0:
        return 'AG'
    result = sum(lista)
    n = len(lista)
    a1 = lista[0]
    r = lista[1]-lista[0]
    q = lista[1]/lista[0]
    if result == a1*n + n*(n-1)*r*0.5:
        if result == a1*(q**n - 1)/(q - 1):
            return 'AG'
        else:
            return 'PA'
    elif result == a1*(q**n - 1)/(q - 1):
        return 'PG'
    else:
        return 'NA'