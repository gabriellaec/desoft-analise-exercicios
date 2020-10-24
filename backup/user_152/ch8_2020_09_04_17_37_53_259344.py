def calcula_posicao (instante, posicaoinicial, velocidade):
    posicao = posicaoinicial + velocidade * instante
    return posicao

t = int(input("Entre com o instante: "))
so = int(input("Entre com a posição inicial: "))
v = int(input("Entre com a velocidade: "))
s = calcula_posicao(t, so, v)
print("A posição no instante {0} é {1} ." .format(t, s))