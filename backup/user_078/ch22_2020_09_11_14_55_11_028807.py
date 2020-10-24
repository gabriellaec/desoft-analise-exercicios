cigas_dia = int(input('Quantos cigarros p/ dia? '))
anos_fumante = int(input('Fuma há quantos anos? '))

dias_fumante = anos_fumante * 365

total_cigas_fumados = dias_fumante * cigas_dia

reducao_expectativa_dias = ((total_cigas_fumados * 10)/60)/24

print ('Você perdeu {0} dias de vida'.format(reducao_expectativa_dias))