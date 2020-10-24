cigarros_dia = int(input('Quantos cigarros você fuma por dia? '))
anos_fumando = int(input('Há quantos anos você fuma? ')) 
dias_fumando = anos_fumando * 365
minutos_perdidos = cigarros_dia * 10 * dias_fumando
dias_perdidos = minutos_perdidos / 60
print(dias_perdidos)