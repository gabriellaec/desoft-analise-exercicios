def interseccao_valores(dic1,dic2):
    lista = []
    for v in dic1.values():
        for e in dic2.values():
            if v==e and e not in lista:
                lista.append(e)
                