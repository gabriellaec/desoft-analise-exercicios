qtde_cigarros = int(input('Quantos cigarros você fuma por dia?'))
qtde_anos = float(input('Há quantos anos você fuma?'))

def tempo_perdido(qtde_cigarros, qtde_anos):
    y = qtde_cigarros*365*qtde_anos/144
    return y
    
c = tempo_perdido(qtde_cigarros, qtde_anos)
print(c)