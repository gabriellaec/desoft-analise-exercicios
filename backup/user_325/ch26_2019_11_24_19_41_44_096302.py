def total(dias, horas, minutos, segundos):
    d = dias * 86400
    h = horas * 3600
    m = minutos * 60
    soma = d + h + m + segundos
    return soma

dias = int(input("quantidade de dias"))
horas = int(input("quantidade de horas"))
minutos = int(input("quantidade de minutos"))
segundos = int(input("quantidade de segundos"))

print(total(dias, horas, minutos, segundos))