def calcula_posicao(instante, posição_inicial, velocidade):
	posicao = posição_inicial + velocidade*instante
	return posicao

print (calcula_posicao(pi, 5, 8))