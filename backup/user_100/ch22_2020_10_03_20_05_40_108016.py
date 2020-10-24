pergunta = int(input('Quantos cigarros você fuma por dia?'))
pergunta2 = int(input('Voocê fuma a quanto tempo?'))

def tempo_perdido(pergunta, pergunta2):
    t = pergunta * 10 * pergunta2
    return t

print(tempo_perdido)