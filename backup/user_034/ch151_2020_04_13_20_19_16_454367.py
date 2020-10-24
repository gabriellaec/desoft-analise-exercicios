def classifica_lista(lista):
    if len(lista) < 2:
        return "nenhum"
    a = lista[1]-lista[0]
    elif a > 0:
        for e in range(len(lista)-1):
            if lista[e+1]-lista[e]<=0
            return "nenhum"
    elif a < 0:
        for e in range(len(lista) -1):
            if lista[e+1]-lista[e]>=0
            return "nenhum"
    elif a == 0:
        return "nenhum"
    elif a > 0:
        return "crescente"
    elif a < 0:
        return "decrescente"