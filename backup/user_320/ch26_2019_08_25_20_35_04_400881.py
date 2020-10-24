dias = int(input('quantos dias: '))
horas = int(input('Quantas horas: '))
minutos = int(input('Quantos minutos: '))
segundos = int(input('Quantos segundos: '))

dias = dias * 24* 60 *60
horas = horas *60*60
minutos = minutos * 60
segundos = segundos + dias + horas + minutos
print(segundos)