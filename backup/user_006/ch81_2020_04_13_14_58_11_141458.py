def interseccao_valores(d1, d2):
    lista=[]
    for i in d1.values():
        for g in d2.values():
            if i==g:
                lista.append(i)
    return lista