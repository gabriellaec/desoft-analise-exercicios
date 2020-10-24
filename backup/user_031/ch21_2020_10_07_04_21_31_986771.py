dias= int(input('Numero de dias: '))
horas= int(input('Numero de horas: '))
minutos=int(input('Numero de minutos: '))
segundos= int(input('Numero de segundos: '))
segundosD= dias * 24 * 60 * 60
segundosH= horas * 60 * 60
segundosM= minutos * 60
segundosT= segundosD + segundosH + segundosM + segundos
print(segundosT)