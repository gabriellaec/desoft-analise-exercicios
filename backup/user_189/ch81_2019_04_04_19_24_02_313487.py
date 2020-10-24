def interseccao_valores(dic1.value,dic2.value):
    lista=[]
    for a in dic1.value:
        for b in dic2.value:
            if a==b:
                lista.append(a)
        return lista
