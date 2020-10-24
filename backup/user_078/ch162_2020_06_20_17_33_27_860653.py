def verifica_lista(lista_numeros):

    lista_pares = []
    lista_impares = []

    if len(lista_numeros) > 0:

        for numero in lista_numeros:

            if numero % 2 == 0:
                lista_pares.append(numero)
            
            else:
                lista_impares.append(numero)

        if len(lista_impares) > 0 and len(lista_pares) == 0:
            return 'ímpar'

        elif len(lista_pares) > 0 and len(lista_impares) == 0:
            return 'par'

        else:
            return 'misturado'

    else:
        return 'misturado'