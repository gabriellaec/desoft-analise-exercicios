def calcula_velocidade_media(Distancia_percorrida,Tempo_gasto):
    velocidade_media = Distancia_percorrida/Tempo_gasto
    return velocidade_media


Distancia_percorrida = int(input('Quantos km foram percorridos? '))
Tempo_gasto = int(input('Quantas horas foram gastas? '))
Velocidade_media = calcula_velocidade_media(Distancia_percorrida,Tempo_gasto)
print(Velocidade_media )