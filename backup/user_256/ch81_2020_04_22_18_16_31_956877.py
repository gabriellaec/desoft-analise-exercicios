def  interseccao_valores(d1, d2):
    lista =[]
    for valores in d1.values():
        if valores in d2.values():
            lista.append(valores)
    return lista
        