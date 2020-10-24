d=int(input('quantidade de dias:'))
h=int(input('quantidade de horas:'))
m=int(input('quantidade de minutos:'))
s=int(input('quantidade de segundos:'))
print('a quantidade de segundos é: ', tempo_total(d, h, m, s))
def tempo_total(dias, horas, minutos, segundos):
    y=dias*24*3600 + horas * 3600 + minutos * 60 + segundos
    return y
