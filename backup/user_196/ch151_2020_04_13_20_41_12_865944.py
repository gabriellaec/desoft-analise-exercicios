def classifica_lista(lista):
    for i in range (len(lista)):
        if lista[i] < lista[i-1]:
            return "decrescente"
        elif lista[i] > lista[i+1]:
            return "crescente"
        else:
            return "nenhum"
    if len(lista) < 2:
        return "nenhum"