def posicoes_minusculas(s):
    lista=[]
    for i, j in enumerate(s):
        if j.islower() == True:
            lista.append(i)
    return(lista)