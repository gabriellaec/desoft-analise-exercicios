def interseccao_chaves (x,y):
    lista =[] 
    for chavex in x.keys():
        for chavey in y.keys():
            if chavex==chavey:
                lista.append (chavex)
    return lista