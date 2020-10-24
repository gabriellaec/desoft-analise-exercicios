def classifica_lista(lista):
    if len(lista) < 2:
        return "nenhum"
    else:
        for e in range(len(lista)):
            if lista[e] > lista[e+1] and lista[e+1] < lista[e+2]:
                return "nenhum"
            elif lista[e] > lista[e+1]:
                return "decrescente"
            elif lista[e] < lista[e+1]:
                return "crescente"
            else:
                return "nenhum"