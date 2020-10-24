def classifica_lista(lista):
    if len(lista) < 2:
        return "nenhum"
    else:
        for e in range(len(lista)-1):
            if lista[e] > lista[e+1]:
                if lista[e+1] < lista[e+2]:
                    return "nenhum"
                else:
                    return "decrescente"
            elif lista[e] < lista[e+1]:
                if lista[e+1] > lista[e+2]:
                    return "nenhum"
                else:
                    return "crescente"
            else:
                return "nenhum"