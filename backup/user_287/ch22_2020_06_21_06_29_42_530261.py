temp_anos =  int(input('há quantos anos fuma: '))
quant = int(input('quantos cigarros por dia: '))
total = (quant * 365 * temp_anos * 10) /525600
print('Expectativa de vida reduzida em',total,'anos')