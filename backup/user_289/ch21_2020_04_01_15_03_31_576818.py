DIAS= int(input('Qual é a quantidade de dias?'))
HORAS= int(input('Qual é a quantidade de horas?'))
MINUTOS= int(input('Qual é a quantidade de minutos?'))
SEGUNDOS= int(input('Qual é a quantidade de horas?'))

TOTAL = DIAS*24*60*60 + HORAS*60*60 + MINUTOS*60 + SEGUNDOS
print(TOTAL)