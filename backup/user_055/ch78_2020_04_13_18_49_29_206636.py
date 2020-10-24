from math import sqrt
def calcula_tempo(atletas_aceleracao):
    tempo_conclusao = {}
    s = 100
    for atleta, aceleracao in atletas_aceleracao.items():
        tempo_conclusao[atleta] = sqrt((2*s)/aceleracao)
    print('O vencedor é {0} com tempo de conclusão de {1} s'.format(atleta, tempo_conclusao[atleta]))

atletas_competicao = {}
atletas = input('Digite o nome do atleta: ')
aceleracoes = int(input('Digite a aceleração do atleta: '))
maior_aceleracao = 0
melhor_atleta = 'x'
while atletas != 'sair':
    if aceleracoes > maior_aceleracao:
        melhor_atleta = atletas
        maior_aceleracao = aceleracoes
    atletas = input('Digite o nome do atleta: ')
    if atletas == 'sair':
        break
    aceleracoes = int(input('Digite a aceleração do atleta: '))
atletas_competicao[melhor_atleta] = maior_aceleracao
calcula_tempo(atletas_competicao)