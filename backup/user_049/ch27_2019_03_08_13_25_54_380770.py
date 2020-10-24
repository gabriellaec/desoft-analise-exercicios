cigarros = int(input('Quantos cigarros voce fuma por dia?'))
anos = int(input('Quantos anos voce fuma? '))
def tempo_perdido(cigarros, anos):
    y=anos*365*cigarros*1.0/144
    return y
print (tempo_perdido(cigarros, anos))