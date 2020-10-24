def posicoes_minusculas(s):
    lista = []
   
    for i in s:
        if s[i].islower() == True:
            lista.append(i)
    return lista