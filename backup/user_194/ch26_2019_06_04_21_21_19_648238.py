dias = int(input('quantos dias?'))
horas = int(input('quantas horas?'))
minutos = int(input('quantos minutos?'))
segundos = int(input('quantos segundos?'))

total = (dias/86400)+(horas/3600)+(minutos/60)+segundos

print(total)