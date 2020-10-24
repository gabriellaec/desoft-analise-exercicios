def calcula_posicao(posicao_inicial, velocidade, instante):
    if velocidade < 0 or instante < 0 or posicao_inicial < 0:
        return False
    else:
        return posicao_inicial+velocidade*instante