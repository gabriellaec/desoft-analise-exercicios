cigarrosDia = int(input('Quantos cigarros você fuma por dia? '))
fumaAnos = int(input('Há quantos anos você fuma? '))

cigarrosAno= cigarrosDia*fumaAnos
tempo_de_cigarros = cigarrosAno*365*24*60
print('Tempo de vida perdido: {0}'.format(tempo_de_cigarros/10))
 