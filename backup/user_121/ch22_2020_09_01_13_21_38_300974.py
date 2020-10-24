quantidade = int(input('Quantos cigarros você fuma por dia? '))
anos = int(input('Há quantos anos você fuma? '))

def f(x, y):
    tempo_perdido = x * 365 * y / 144
    resultado = print('Você já perdeu {:.0f} dias de vida'.format(tempo_perdido))
    return resultado
    
f(quantidade, anos)