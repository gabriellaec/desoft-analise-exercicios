def interseccao_valores(dic1,dic2):
    lista=[]
    i=0
    for a in dic1.value(i):
        for b in dic2.value(i):
            if a in dic1.value==b in dic2.value(i):
                lista.append(a)
                i+=1
        return lista