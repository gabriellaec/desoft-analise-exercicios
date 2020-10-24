def traduz(lista,dicio):
    listareesp=[]
    for el in lista:
        for l , m in dicio.items():
            if el==l:
                listareesp.append(m)
    return listareesp