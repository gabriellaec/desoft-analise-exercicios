def interseccao_valores(dicionario1, dicionario2):
    lista=[]
    for v in dicionario1:
        for v2 in dicionario2:
            if v == v2:
                lista.append(v)
    return lista
       
    
        