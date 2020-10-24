anos= int(input('A quantos anos você fuma? '))
cigarros = int(input('Quantos cigarros fuma por dia? '))
def tempo_perdido(anos, cigarros):
    tempo_perdido = anos*365*cigarros*10
    print('Você fumou {0} dias da sua vida'.format(tempo_perdido))
    return "a"
tempo_perdido(anos, cigarros)