cigarros = int(input('Quantos cigarros voce fuma por dia?))
anos = int(input('Quantos anos voce fuma? '))
def tempo_perdido(cigarros, anos):
    y=int(anos)*365*int(cigarros)*1/8640
    return y
print (tempo_perdido(cigarros, anos))