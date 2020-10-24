def verifica_primos (lista):
    dicionário = {}
    for i in range(len(lista)):
        for numero, booleano in dicionário.items():
            if numero not in dicionario:
                if lista[i] == 0 or lista[i] == 1:
                    dicionário['numero'] = False
                elif lista[i] ==2:
                    dicionário['numero'] = True
                j = 3
                while j < i:
                    if lista[i] % 2 == 0:
                        dicionário['numero'] = False
                    if lista[i] % j == 0:
                        dicionário['numero'] = False
                    j = j + 2
                else:
                    dicionário['numero'] = True    
    return  dicionário                   