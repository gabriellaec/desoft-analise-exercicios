def traduz(x, y):
    lista = []
    for i in range(len(x)):
        for ing, port in y.items():
                if x[i] == ing:
                    lista.append(y[ing])
    return lista               
                    