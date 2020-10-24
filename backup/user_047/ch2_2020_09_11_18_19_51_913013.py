def calcula_velocidade_media(distancia,tempo_gasto):
    distancia_m = distancia*1000
    tempo_gasto_s = (tempo_gasto*60)*60
    velocidade = distancia_m/tempo_gasto_s
    velocidade_km = velocidade*3.6
    return velocidade_km