def interseccao_valores(d1,d2):
    lista=[]
    for i in d1.valus():
        if i in d2.valus():
            lista.append(i)
    return lista