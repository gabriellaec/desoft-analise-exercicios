def tempo_perdido(cigarros_por_dia,tempo):
    tp = (10/60/24) * cigarros_por_dia * (tempo*365)
    return tp
cigarros_por_dia = int(input('Quantos cigarros fuma por dia? '))
tempo = int(input('Há quantos anos fuma? '))
print(tempo_perdido(cigarros_por_dia,tempo))