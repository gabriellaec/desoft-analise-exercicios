dias = input('Quantos dias?')
print(dias)
horas = input('Quantas horas?')
print(horas)
minutos = input('Quantos minutos?')
print(minutos)
segundos = input('Quantos segundos?')
print(segundos)

def total_segundos (dias, minutos, segundos):
    y = (24*60*60*dias)+(60*60*horas)+(60*minutos)+(segundos)
    return y

print(total_segundos)