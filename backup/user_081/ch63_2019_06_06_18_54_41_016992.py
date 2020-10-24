
def pos_arroba(x):
    valido = False
    for i in x:
        if x[i] =="@":
            valido = True
			posicao = i
    return posicao
                