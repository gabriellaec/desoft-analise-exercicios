def classifica_lista(lista):
    if len(lista) < 2:
        return nenhum
    for i in range(len(lista)-1):
        if lista[i+1] < lista[i]:
            break
        if i == len(lista)-2:
            return "crescente"
        
    for i in range(len(lista)-1):
        if lista[i+1] > lista[i]:
            break
        if i == len(lista)-2:
            return "decrescente"
    return "nenhum"