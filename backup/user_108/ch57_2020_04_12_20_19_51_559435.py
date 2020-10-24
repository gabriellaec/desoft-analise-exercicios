def verifica_progressao(lista):
    r = lista[1] - lista[0]
    q = lista[1] / lista[0]
    
    pa = [lista[0] + i*r for i in range(len(lista))]
    pg = [lista[0] * r**i for i in range(len(lista))]
    
    if lista == pg:
        return "PG"
    if lista == pa:
        return "PA"
    return "NA"
    