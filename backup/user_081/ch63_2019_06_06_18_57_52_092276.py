
def pos_arroba(x):
    valido = False
    for i in range(0,len(x)):
        if x[i] =="@":
            valido = True
            if valido:
                posicao = i
    return posicao
                