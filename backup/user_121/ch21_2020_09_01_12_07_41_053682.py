dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))

def f(a, b, c, d):
    dias_em_segundos = a * 86400
    horas_em_segundos = b * 3600
    minutos_em_segundos = c * 60
    segundos_em_segundos = d
    total = print(dias_em_segundos + horas_em_segundos + minutos_em_segundos + segundos_em_segundos)
    return total

f(dias, horas, minutos, segundos)