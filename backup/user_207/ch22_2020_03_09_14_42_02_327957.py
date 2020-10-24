cigarros_por_dia = int (input('Quantos cigarros você fuma por dia? '))
tempo_em_anos = int (input ('Há quantos anos ? '))

def reducao_do_tempo_de_vida (cigarros_por_dia, tempo_em_anos):
    y = 10* (cigarros_por_dia * 365 * tempo_em_anos) /   (60*24)
    return y

print (reducao_do_tempo_de_vida(cigarros_por_dia, tempo_em_anos))
