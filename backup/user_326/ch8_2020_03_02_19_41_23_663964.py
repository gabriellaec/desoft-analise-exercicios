def calcula_posicao(distancia, tempo, velocidade):
    sorvete = distancia + velocidade*tempo
    return sorvete


movimento = calcula_posicao(1, 2, 3)

print(movimento)
