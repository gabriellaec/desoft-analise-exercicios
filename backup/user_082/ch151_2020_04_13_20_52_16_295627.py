def classifica_lista(lista_numeros):
    if len(lista_numeros) == 2 or len(lista_numeros) == 0:
        return ("nenhum")
    else:
        for i in lista_numeros:
            if lista_numeros[i] > lista_numeros[i + 1]:
                return ("decrescente")
            elif lista_numeros[i + 1] > lista_numeros[i]:
                return ("crescente")
            else:
                return("nenhum")
