def interseccao_valores(dic1, dic2):
    lista = []
    for m in dic1.values():
        for n in dic2.values():
            if n == m:
                lista.append(n)
    print(lista)           