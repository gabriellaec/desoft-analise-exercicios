def posicoes_minusculas(s):
    c=[]
    for i in s:
        if s[i].islower()==True:
            c.append(i)
    return c