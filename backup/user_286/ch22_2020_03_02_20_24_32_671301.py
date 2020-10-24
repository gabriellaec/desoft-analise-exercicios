cigarros_dia = int(input('Cigarros por dia? '))
anos = int(input('Há quantos anos? '))

total_cigarros = (anos*365*cigarros_dia)/(6*24)

print('Voce perdeu {0} dias de vida'.format(total_cigarros))