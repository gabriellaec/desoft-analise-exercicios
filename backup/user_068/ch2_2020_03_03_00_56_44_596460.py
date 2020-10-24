def calcula_velocidade_media(distância1, tempo1, distância2, tempo2)
	calcula_velocidade_média = (distância2 - distância1) / (tempo2 - tempo1)
    return calcula_velocidade_média
resultado = calcula_velocidade_média(10, 2, 20, 4)
print(resultado)
