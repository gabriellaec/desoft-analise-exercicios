def nome_usuario(n):
    posicao=0
    i=0
    while i<len(n):
        if n[i]!='@':
            posicao+=1
        else:
            break
        i+=1
    return n[:posicao]