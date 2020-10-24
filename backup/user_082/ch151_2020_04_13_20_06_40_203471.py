def classifica_lista(lista_numeros):
    if len(lista) == 2:
        return ("nenhum")
    else:
        for i in len(lista_numeros):
            if lista_numeros[i] > lista_numeros[i + 1]:
                return ("decrescente")
            elif lista_numeros[i + 1] > lista_numeros[i]:
                return ("crescente")
            else:
                return("nenhum")
