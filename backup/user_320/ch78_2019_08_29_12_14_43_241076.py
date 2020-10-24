from math import sqrt

nomes = {}
while True:
    nome = input('Digite o nome: ')
    if nome == 'sair':
        break
    acele = float(input('Digite a aceleração: '))
    nomes[nome] = acele


def calcula_tempo(dic):
    tempo = {chave: sqrt(200/valor) for chave, valor in dic.items()}
    return tempo

print(calcula_tempo(nomes))