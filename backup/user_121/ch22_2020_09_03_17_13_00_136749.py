quantidade = int(input('Quantos cigarros você fuma por dia? '))
anos = int(input('Há quantos anos você fuma? '))

def calcula_tempo_perdido(x, y):
    if y == 0:
        tempo_perdido = x // 144
    else:
        tempo_perdido = x * 365 * y // 144
    resultado = print('Você já perdeu {} dias de vida'.format(tempo_perdido))
    return resultado
    
calcula_tempo_perdido(quantidade, anos)