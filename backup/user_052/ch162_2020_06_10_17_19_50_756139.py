def verifica_lista (lista_numeros):
    if lista_numeros == []:
        return ("misturado")
    else: 
        ímpar = True
        par = True
        misturado = False
        i = 0
        while i < len(lista_numeros):
            if lista_numeros[i] % 2 == 0:
                ímpar = False
                i += 1
                if lista_numeros[i] % 2 != 0:
                    misturado = True
                    return ("misturado")
                    i += 1
                else:
                    return ("par")
                    i += 1
            elif lista_numeros[i] % 2 != 0:
                par = False
                i += 1
                if lista_numeros[i] % 2 == 0:
                    misturado = True
                    return ("misturado")
                    i += 1
                else:
                    return ("ímpar")
                    i += 1

            