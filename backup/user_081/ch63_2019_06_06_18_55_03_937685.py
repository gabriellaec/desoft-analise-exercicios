
def pos_arroba(x):
    valido = False
    for i in range (0,x+1):
        if x[i] =="@":
            valido = True
			posicao = i
    return posicao
                