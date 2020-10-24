dias = int(input("Digite uma quantidade de dias:"))
horas = int(input('Digite uma quantidade de horas:'))
minutos = int(input('Digite uma quantidade de minutos:'))
segundos = int(input('Digite uma quantidade de segundos:'))
def quantos_segundos(dias,horas,minutos,segundos):
    segs = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos
    return segs
print(quantos_segundos(dias,horas,minutos,segundos))