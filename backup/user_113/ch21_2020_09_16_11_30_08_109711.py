dias = int(input('Quantos dias?: '))
horas = int(input('Quantas horas?: '))
minu = int(input('Quantos minutos?: '))
seg = int(input('Quantos segundos?: '))

tempo = seg + (minu * 60) + (horas * 3600) + (dias * 86400)
print(tempo)