def quantos_uns(n):
    numero=str(n)
    posicao=0
    uns=0
    while posicao<len(numero):
        if numero[posicao]=='1':
            uns+=1
        posicao+=1
    return uns