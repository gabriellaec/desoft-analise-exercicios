def classifica_lista(lista):
    if (len(lista)<2):
        return 'nenhum'
    z = lista[1] - lista[0]
    if z>0:
        for i in range (len(lista)-1):
            if lista[i] - lista[i+1] <= 0:
                return'nenhum'
    if z<0:
        for i in range (len(lista)-1):
            if lista[i] - lista[i+1] >= 0:
                return 'nenhum'
    if z==0:
        return "nenhum"
    elif z<0:
        return "decrescente"
    elif z>0:
        return "crescente"