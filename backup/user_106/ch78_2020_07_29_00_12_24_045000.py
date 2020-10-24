import math

def calcula_tempo(dic):
    novo = {}
    for i in dic:
        novo[i] = (200 / dic[i]) ** 0.5
    return novo


dicio = {}
nome = input('Nome do atleta: ')
while nome != 'sair':
    dicio[nome] = input('Aceleração do atleta: ')

tempos = calcula_tempo(dicio)
menor = math.inf
for i in tempos:
    if tempos[i] < menor:
        menor = tempos[i]
        vencedor = i
        
print('O vencedor é {0} com tempo de conclusão de {1} s'.format(vencedor, tempos[vencedor]))