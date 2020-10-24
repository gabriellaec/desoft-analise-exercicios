from math import*
def calcula_tempo(dicionario_atletas):
    dict = {}
    for atleta, aceleracao in dicionario_atletas.items():
        dict[atleta] = sqrt(200/aceleracao)
    return dict
dict = {}
nome = str(input('Digite o nome: '))
while nome != 'sair':
    aceleracao = float(input('Digite a aceleração: '))
    dict[nome] = sqrt(200/aceleracao)
    nome = str(input('Digite o nome: '))
dicionario = calcula_tempo(dict)
menor_tempo = 100
for atleta, tempo in dict.items():
    if tempo < menor_tempo:
        menor_tempo = tempo
        vencedor = atleta
print('O vencedor é {0} com tempo de conclusão de {1} s'.format(vencedor, menor_tempo))
    