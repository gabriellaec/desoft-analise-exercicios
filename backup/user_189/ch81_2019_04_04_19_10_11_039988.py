def interseccao_valores(dic1,dic2):
    lista=[]
    i=0
    for a in dic1[i]:
        for b in dic2[i]:
            i+=1
            if a==b:
                lista.append(a)
    return(lista)
