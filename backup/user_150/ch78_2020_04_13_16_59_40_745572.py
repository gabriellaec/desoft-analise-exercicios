from math import *

dicionario_digitado = {}

while True:
    nome_atleta = input('Qual o nome do atleta? ')
    if nome_atleta == 'sair':
        break
    else:
        dicionario_digitado[nome_atleta] = int(input('Qual a aceleração do atleta? '))
    for k, v in dicionario_digitado.items():
        dicionario_digitado[k] = sqrt(200/v)

    tempo = list(dicionario_digitado.values())
    atletas = list(dicionario_digitado.keys())

    print('O vencedor é {1} com tempo de conclusão de {0} s'.format(min(tempo), atletas[tempo.index(min(tempo))]))