def calcula_velocidade_media(d,t):
    v=d/t
    return v
d=int(input('Distância percorrida: '))
t=int(input('Tempo gasto: '))
print('A velocidade média é: {0}km/h'.format (calcula_velocidade_media(d,t)))