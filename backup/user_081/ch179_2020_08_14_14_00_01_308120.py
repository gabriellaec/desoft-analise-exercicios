def posicoes_minusculas(s):
    lista=[]
    for i in s:
        if s[i].islower():
            lista.append(s[i])
    return lista
            