def interseccao_valores(dic1, dic2):
    lista = []
    for m in dic1:
        for n in dic2:
            if n in m:
                lista.append(n)
    print(lista)           