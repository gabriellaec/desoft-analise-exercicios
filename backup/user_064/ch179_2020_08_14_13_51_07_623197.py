def posicoes_minusculas(s):
    lista = []
    contador = 0
    for i in s:
        if i.islower() == True:
            lista.append(contador)
            contador +=1
        else:
            contador+=1
    return lista