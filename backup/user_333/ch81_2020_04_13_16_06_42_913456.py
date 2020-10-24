def interseccao_valores(d1,d2):
    valores=[]
    d1_values=d1.values()
    for e in d1_values:
        if e in d2.values():
            valores.append(e)
    return valores