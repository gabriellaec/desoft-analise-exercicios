def nome_usuario(x):
    valido = False
    for i in range(0,len(x)):
        if x[i] =="@":
            valido = True
            posicao = i
            if valido:
                nome = x[:i]
    return nome