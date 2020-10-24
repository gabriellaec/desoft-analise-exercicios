def verifica_lista (lista_numeros):
    if lista_numeros == []:
        return ("misturado")
    else: 
        ímpar = True
        par = True
        for i in range(len(lista_numeros)-1):
            if lista_numeros[i] % 2 == 0:
                ímpar = False
            else:
                par = False
        if ímpar:
            print ("ímpar")
        elif par:
            print ("par")
        else:
            print ("misturado")
            