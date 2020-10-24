lista_class = []
def classifica_lista(lista):
    if len(lista) < 2:
        classificacao = "nenhum"
    for i in range(len(lista)-1):
        if lista[i+1] > lista[i]:
            classificacao = "crescente"
            lista_class.append(classificacao)
        elif lista[i+1] < lista[i]:
            classificacao = "decrescente"
            lista_class.append(classificacao)
        else:
            classificacao = "nenhum"
    if len(lista_class) > 0:
        j = 0
        while j != len(lista_class) - 1:
            if lista_class[j] != lista_class[j+1]:
                classificacao = "nenhuma"
            else:
                return classificacao
            j += 1
    return classificacao