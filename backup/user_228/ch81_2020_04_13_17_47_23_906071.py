def interseccao_valores(pires,parnes):
    lista=list(pires.values())
    lista1=list(parnes.values())
    lista2=[]
    for i in lista:
        for j in lista1:
            if j==i:
                lista2.append(i)
    return lista2
