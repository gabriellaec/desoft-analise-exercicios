def verifica_lista (lista_numeros):
    if lista_numeros == []:
        return ("misturado")
    else: 
        ímpar = True
        par = True
        misturado = False
        i = 0
        for i in range(len(lista_numeros)-1):
            if lista_numeros[i] % 2 == 0:
                ímpar = False
                if lista_numeros[i] % 2 != 0:
                    misturado = True
                    return ("misturado")
                else:
                    return ("par")
            elif lista_numeros[i] % 2 != 0:
                par = False
                if lista_numeros[i] % 2 == 0:
                    misturado = True
                    return ("misturado")
                else:
                    return ("ímpar")

            