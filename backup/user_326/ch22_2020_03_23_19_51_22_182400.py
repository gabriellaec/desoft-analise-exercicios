bitucas = int(input('quantos cigarros você fuma por dia? '))
anos = int(input('a quantos anos fuma? '))

tempo_perdido = (bitucas * (1/144)) * (anos * 365) 
print('você perdeu {} dias de sua vida'.format(tempo_perdido))