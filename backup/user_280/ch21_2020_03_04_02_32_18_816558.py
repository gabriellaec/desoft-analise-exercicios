def total_segundos(dias, horas, minutos, segundos):
    y = (24*60*60*dias)+(60*60*horas)+(60*minutos)+(segundos)
    return y

dias = input('Quantos dias?')
horas = input('Quantas horas?')
minutos = input('Quantos minutos?')
segundos = input('Quantos segundos?')
print(total_segundos)