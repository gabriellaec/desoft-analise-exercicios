def verifica_primos(lista):
    dicionario = {}
    for i in lista:
        if i == 2 or i == 3:
            dicionario[i] = True
        elif i%2 == 0 or i == 1:
            dicionario[i] = False
        else:
            dicionario[i] = True
            for x in range(3,i,2):
                if i%x == 0:
                    dicionario[i] = False
    return dicionario