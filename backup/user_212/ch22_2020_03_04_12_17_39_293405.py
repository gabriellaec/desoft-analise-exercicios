cigarros=int(input('quantos cigarros você fuma por dia'))
tempo=int(input('há quanto tempo você fuma'))

total_cigarros= cigarros*tempo
minutos_perdidos= total_cigarros*10
dias_perdidos= minutos_perdidos/1440

print(dias_perdidos)