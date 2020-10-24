def interseccao_valores(dic1,dic2):
    lista=[]
    for a in dic1.value:
        for b in dic2.value:
            if a in dic1.value==b in dic2.value:
                lista.append(a)
        return lista
