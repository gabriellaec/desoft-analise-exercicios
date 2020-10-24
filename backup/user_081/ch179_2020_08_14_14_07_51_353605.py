def posicoes_minusculas(s):
    lista=[]
    for i in s:
        if i.islower():
            lista.append(s.index(i))
    return lista
            