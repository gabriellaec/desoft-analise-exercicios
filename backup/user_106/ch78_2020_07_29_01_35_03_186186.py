def calcula_tempo(ace):
    tempo = {}
    for nome in ace:
        tempo[nome] = (200 / ace[nome]) ** 0.5
        menor = tempo[nome]
    for a in tempo:
        if tempo[a] < menor:
            menor = tempo[a]
            vencedor = a
    final = print('O vencedor é {0} com tempo de conclusão de {1} s'.format(vencedor, tempo[vencedor]))
    return final

dicio = {}
nome = input('Nome do atleta: ')
while nome != 'sair':
    dicio[nome] = input('Aceleração do atleta: ')
    
calcula_tempo(dicio)