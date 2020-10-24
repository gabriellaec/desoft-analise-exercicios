import math
nomes_aceleracao = {}
nome = input('Nome ')
while nome != 'sair':
    aceleracao = float(input('Aceleração '))
    nomes_aceleracao[nome] = aceleracao
    nome = input('Nome ')
def calcula_tempo(nomes_aceleracao):
    tempo_conclusao = {}
    for k, v in nomes_aceleracao.items():
        if v == 0:
            tempo_conclusao[k] = 'Não concluiu'
        else:
            tempo_conclusao[k] = math.sqrt(200/v)
    return tempo_conclusao
dicionario = calcula_tempo(nomes_aceleracao)
menor_tempo = 3600
vencedor = ''
for p, v in calcula_tempo(nomes_aceleracao).items():
    if v < menor_tempo:
        menor_tempo = v
        vencedor = p
print('O vencedor é {} com tempo de conclusão de {} s.'.format(vencedor, menor_tempo))