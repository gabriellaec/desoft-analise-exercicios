def interseccao_chaves(dic1,dic2):
    lista=[]
    for a in dic1:
        for b in dic2:
            if a==b:
                lista.append(a)
    return lista