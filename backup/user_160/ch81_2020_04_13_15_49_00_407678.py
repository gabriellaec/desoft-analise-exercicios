def interseccao_valores(dic1, dic2):
    dic1.values()
    dic2.values()
    lista = []
    for m in dic1:
        for n in dic2:
            if n == m:
                lista.append(n)
    print(lista)           