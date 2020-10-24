def interseccao_valores(dic1,dic2):
    lista=[]
    i=0
    z=0
    for a in dic1.value(i):
        i+=1
        for b in dic2.value(z):
            z+=1
            if a in dic1.value(i)==b in dic2.value(z):
                lista.append(a)
        return lista