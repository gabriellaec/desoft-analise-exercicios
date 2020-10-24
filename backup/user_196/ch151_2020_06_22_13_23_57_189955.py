def classifica_lista(lista):
    if len(lista) < 2:
        return "nenhum"
    listacrescente = [lista[0]]
    listadecrescente = [lista[0]]
    maior = lista[0]
    menor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > maior:
            listacrescente.append(lista[i])
            maior = lista[i]
        elif lista[i] < menor:
            listadecrescente.append(lista[i])
            menor = lista[i]
         
    if lista == listacrescente:
        return "crescente"
    elif lista == listadecrescente:
        return "decrescente"
    else:
        return "nenhum"