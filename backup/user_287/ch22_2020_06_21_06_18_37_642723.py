quant = int(input('quantos cigarros por dia: '))
temp_anos =  int(input('há quantos anos fuma: '))

dias_fumando = 365 * temp_anos

total_cigarros = quant * dias_fumando

total_min = total_cigarros * 10

total_ano = total_min/525600

print(total_ano)