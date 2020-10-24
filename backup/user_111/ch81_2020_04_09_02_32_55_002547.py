def interseccao_valores(dic1,dic2):
    lista=[]
    for i in dic1.value():
        for j in dic2.value():
            if i==j:
                lista.append(i)
    return lista