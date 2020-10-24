def tempo_perdido(cigarros,anos):
    tempo = (10/60/24)*cigarros*anos*365
    return tempo

cigarros = int(input('Quantos cigarros vc fuma por dia? '))
anos = int(input('A quantos anos vc fuma? '))
print(tempo_perdido(cigarros,anos))