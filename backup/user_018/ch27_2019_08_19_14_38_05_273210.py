cigarros = int ( input ( 'Quantos cigarros você fuma por dia?' ))
anos = int ( input ( ' Há quantos anos você fuma? ' ))

dias_perdidos = (cigarros * 10 * anos *365) / (24*60)

print ('Você perdeu {0} dias de vida.' .format(dias_perdidos))
