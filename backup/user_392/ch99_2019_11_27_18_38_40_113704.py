def login_disponivel(x,lista):
    ponto = 0
    if x in lista:
        for e in lista:
            if x == e:
                ponto +=1
    x += ('{0}'.format(ponto))
    return lista