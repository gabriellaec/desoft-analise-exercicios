def verifica_lista (lista_numeros):
    if lista_numeros == []:
        return ("misturado")
    else: 
        ímpar = True
        par = True
        misturado = False
        while i < len(lista_numeros):
            if lista_numeros[i] % 2 == 0:
                ímpar = False
                i += 1
                if lista_numeros[i] % 2 != 0:
                    misturado = True
            elif lista_numeros[i] % 2 != 0:
                par = False
                i += 1
                if lista_numeros[i] % 2 == 0:
                    misturado = True
        if ímpar:
            print ("ímpar")
        elif par:
            print ("par")
        else:
            print ("misturado")
            