temp_anos =  int(input('há quantos anos fuma: '))
quant = int(input('quantos cigarros por dia: '))

total_cigarros = quant * 365 * temp_anos

total_min = total_cigarros * 10

total_ano = total_min/525600

print('Expectativa de vida reduzida em',total_ano,'anos')