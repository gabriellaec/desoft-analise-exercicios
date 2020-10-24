cigarros=int(input('Quantos cigarros vc fuma por dia? '))
tempo=int(input('Há quantos anos? '))
def tempo_perdido(cigarros,tempo):
    TP=(cigarros*tempo*365)/1440
    return TP
print(tempo_perdido(cigarros,tempo))