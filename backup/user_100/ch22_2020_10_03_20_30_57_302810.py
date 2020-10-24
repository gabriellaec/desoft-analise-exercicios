pergunta = int(input('Quantos cigarros você fuma por dia?'))
pergunta2 = int(input('Você fuma a quanto anos?'))

def tempo_perdido(pergunta, pergunta2):
    x = (pergunta * 10) / 1440 
    y = pergunta2 * 365
    z = x * y
    return z

print(tempo_perdido(pergunta, pergunta2)