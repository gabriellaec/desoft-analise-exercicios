def interseccao_chaves(dic1,dic2):
    lista = []
    for i in dic1:
        lista.append(i)
    for i in dic2:
        if i not in dic1:
            lista.append(i)
    