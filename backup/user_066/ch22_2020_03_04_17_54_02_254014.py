anos= int(input('A quantos anos você fuma? '))
cigarros = int(input('Quantos cigarros fuma por dia? '))
def tempo_perdido(anos, cigarros):
	anos_pra_min = anos*365*24*3600
    tempo_perdido_em_dias = anos_pra_min*cigarros*10/24
    print('Você fumou {0} dias da sua vida'.format(tempo_perdido_em_dias)
    return "a"
tempo_perdido(anos, cigarros)