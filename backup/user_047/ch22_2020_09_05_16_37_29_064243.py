numero_cigarros = int(input('digite quantos cigarros voce fuma por dia'))
anos_fumando = int(input(' há quantos anos voce fuma'))*360
minutos_perdidos = numero_cigarros*10*anos_fumando
minutos_para_dias = minutos_perdidos/24
print(minutos_para_dias)