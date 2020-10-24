def calcula_velocidade_media(Distancia_percorrida,Tempo_gasto):
    velocidade_media = Distancia_percorrida/Tempo_gasto
    return velocidade_media


Distancia_percorrida = 500
Tempo_gasto = 10
Velocidade_media = calcula_velocidade_media(Distancia_percorrida,Tempo_gasto)
print(Velocidade_media )