def interseccao_valores(x, y):
    inter=[]
    for valor in x.values():
        for value in y.values():
            if valor == value and valor not in inter:
                inter.append(valor)
    return inter