dias = int(input('Quantos dias?'))
horas = int(input('Quantas horas?'))
minutos = int(input('Quantos minutos?'))
segundos = int(input('Quantos segundos?'))
def conta_tempo(dias, horas, minutos, segundos):
    ds = dias*86400
    hs = horas*3600
    ms = minutos*60
    total = ds + hs + ms + segundos
    return total
print(conta_tempo(dias, horas, minutos, segundos))