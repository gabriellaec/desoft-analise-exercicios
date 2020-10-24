dias = int(input('insira o número de dias: '))
horas = int(input('insira o número de horas: '))
minutos = int(input('insira o número de minutos: '))
segundos= int(input('insira o número de segundos: '))
tot_em_seg = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos
print (tot_em_seg)
