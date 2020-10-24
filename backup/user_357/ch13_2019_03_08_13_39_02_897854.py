def calcula_posicao(posicao_inicial, velocidade, instante):
    if instante < 0:
        return False
    else:
        return posicao_inicial+velocidade*instante