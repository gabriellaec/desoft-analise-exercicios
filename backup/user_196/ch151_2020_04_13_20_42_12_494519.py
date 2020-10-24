def classifica_lista(lista):
    lista = []
    for i in range (1,len(lista)+1):
        if lista[i] < lista[i-1]:
            return "decrescente"
        elif lista[i] > lista[i-1]:
            return "crescente"
        else:
            return "nenhum"
    if len(lista) < 2:
        return "nenhum"