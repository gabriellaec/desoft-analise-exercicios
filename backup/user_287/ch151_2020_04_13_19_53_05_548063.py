def classifica_lista(lista_de_numero):
    if len(lista_de_numero)<2:
        return 'nenhum'
    a = lista_de_numero[1] - lista_de_numero[0]
    if a>0:
        for i in range (len(lista_de_numero)-1):
            if lista_de_numero[i+1] - lista_de_nummero[i] <= 0:
                return 'nenhum'
    if a<0:
        for i in range (len(lista)-1):
            if lista_de_numero[i+1] - lista_de_numero[i] >= 0:
                return "nenhum"
    if a==0:
        return "nenhum"
    elif a>0:
        return "crescente"
    elif a<0:
        return "decrescente"