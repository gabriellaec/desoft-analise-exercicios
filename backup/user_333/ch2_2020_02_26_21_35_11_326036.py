# -*- coding: utf-8 -*-
"""
programa calcula a velocidade media com um input da quantidade de quilometros percorridos e do tempo que demorou para executar a ação

@autor: Francisco Janela
"""
#a função calcula a velocidade média
#distancia_km: distancia percorrida pelo automóvel em km
#tempo: tempo decorrido para percorrer a distância em horas
def calcula_velocidade_media(distancia_km,tempo_h):
    velocidade_media=distancia_km/tempo_h
    return velocidade_media

#os parâmetros abaixo são os inputs dos valores colhidos da distância e do tempo que resultam na velocidade média do automóvel
distancia_em_km=300
tempo_em_horas=5
print('a velocidade média é {0}km/h.'.format(calcula_velocidade_media(distancia_em_km,tempo_em_horas)))
