def calcula_posicao(tempo, posicao_inicial, velocidade):
    y = posicao_inicial + velocidade * tempo
    return y

tempo = 10
posicao_inicial = 5
velocidade = 3
b = calcula_posicao(tempo, posicao_inicial, velocidade)
print (b)