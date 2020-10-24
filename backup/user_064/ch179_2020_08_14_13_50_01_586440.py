def posicoes_minusculas(s):
    lista = []
   
    for i in s:
        if i.islower() == True:
            lista.append(i)
    return lista