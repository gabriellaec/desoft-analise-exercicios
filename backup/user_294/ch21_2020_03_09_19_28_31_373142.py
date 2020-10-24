quantidade_dias = int(input('quantos dias foram'))
horas = int(input('e horas'))
minutos = int(input('minutos'))
segundos = int(input('e segundos?'))
quantidade_segundos= (((quantidade_dias*24)*60)*60)+((horas*60)*60)+(minutos*60)+segundos
print quantidade_segundos