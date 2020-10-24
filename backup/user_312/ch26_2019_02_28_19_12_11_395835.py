def tempo_total(dias, horas, minutos, segundos):
    y=dias*24*3600 + horas * 3600 + minutos * 60 + segundos
    return y
d=int(input('quantidade de dias:\n'))
h=int(input('quantidade de horas:\n'))
m=int(input('quantidade de minutos:\n'))
s=int(input('quantidade de segundos:\n'))
print('a quantidade de segundos é: ', tempo_total(d, h, m, s))