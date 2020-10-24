def posicoes_minusculas(palavra):
    lista=[]
    for i in range (len(palavra)):
        if palavra[i].islower()==True:
            lista.append(i)
    return lista