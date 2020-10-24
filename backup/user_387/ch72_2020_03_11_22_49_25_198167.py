def lista_caracteres(a):
    p = []
    for ele in a:
        if ele not in p:
            p.append(ele)
    return p
