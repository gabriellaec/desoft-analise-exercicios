def interseccao_valores(dicio1,dicio2):
    lista=[]
    for valor in dicio1.values():
        for valor2 in dicio2.values():
            if valor==valor2:
                lista.append(valor)
    return lista
                