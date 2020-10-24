cigarros = int(input('Quantos cigarros fuma por dia?:'))
anos = int(input('Há quantos anos fuma?:'))
def tempo_perdido(cigarros, anos):
    total = (cigarros * (10/1440) * (360 * anos)
    return total
print('O seu tempo de vida perdido em dias é {0:.0f}'.format(tempo_perdido(cigarros,anos)))