dias= int(input('Digite quantos dias: '))
horas= int(input('Digite quastas hora: '))
minutos= int(input('Digite quantos minutos: '))
segundos= int(input('Digite quantos segundos segundo: '))
dias_segundo= dias*24*60*60
horas_segundos= horas*60*60
minuto_segundos= minutos*60
resultado=dias_segundo+horas_segundos+minuto_segundos+segundos
print(resultado)