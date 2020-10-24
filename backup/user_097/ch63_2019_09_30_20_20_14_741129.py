def posicao_arroba(email):
    i = 0
    posicao = -1 #nao colocar 0, colocar -1 pois é a convenção que não achei a posição
    while i < len(email):
        if(email[i]=="@"):
            posicao = i
        i = i + 1
    return posicao