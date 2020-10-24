def posicoes_minusculas(s):
    c=[]
    for i in s:
        if i.islower()==True:
            c.append(s.index(i))
    return c