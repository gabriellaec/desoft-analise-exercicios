def interseccao_valores(pires,parnes):
    lista=pires.values()
    lista1=parnes.values()
    lista2=[]
    for i in lista:
        for j in lista:
            if j==i:
                lista2.append(i)
    return lista2
