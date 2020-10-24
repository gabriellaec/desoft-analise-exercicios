def calcula_velocidade_media(x, y):
    f = x / y
    return(f)

km = int(input('Distância em km:'))
tempo = int(input('Tempo gasto em horas:'))
print(calcula_velocidade_media(km, tempo))
