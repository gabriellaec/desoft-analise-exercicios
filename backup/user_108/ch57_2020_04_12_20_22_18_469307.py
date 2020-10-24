

def verifica_progressao(lista):
    print(lista)
    
    r = lista[1] - lista[0]
    q = lista[1] / lista[0]
    print(q)
    pa = [lista[0] + i*r for i in range(len(lista))]
    pg = [lista[0] * q**i for i in range(len(lista))]
    print(pg)
    if lista == pg:
        return "PG"
    if lista == pa:
        return "PA"
    return "NA"
    