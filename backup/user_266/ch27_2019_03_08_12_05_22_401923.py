cigarros = int(input('quantos cigarros fuma por dia: '))
anos = int(input('quantos anos fuma: '))
dias = anos*365
min = dias*10*cigarros
y = (min)/1440
print('voce perdeu {0:.1f} dias da sua vida'.format(y))