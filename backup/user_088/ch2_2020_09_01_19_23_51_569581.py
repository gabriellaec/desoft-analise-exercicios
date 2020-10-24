def calcula_velocidade_media(tempo,espaco):
    calcula_velocidade_media= espaco/tempo
    return calcula_velocidade_media
tempo=10
espaco=30
print('para um tempo {0} em horas e um espaço {1} em km temos uma velocidade media de {2} km/h'.format(tempo,espaco, calcula_velocidade_media)