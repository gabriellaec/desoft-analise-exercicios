import math

def calcula_tempo(dados_atletas):
    resultados = dict()  
    for nome, aceleracao in dados_atletas.items():
        acel = float(aceleracao)  # Caso as acelerações venham em strings
        tempo_gasto = math.sqrt((2*100)/acel)
        resultados[nome] = tempo_gasto
    
    return resultados

# Interage com usuário e monta dicionário com nomes e acelerações
lista_aceleracoes = []
dados = {}
nome = input('Digite o nome do atleta: ')
while nome != 'sair':
    aceleration = float(input('Digite a aceleração do atleta: '))
    lista_aceleracoes.append(aceleration)
    dados[nome] = aceleration
    nome = input('Digite o nome do atleta: ')

# Monta dicionário com nomes e tempo de prova
x = calcula_tempo(dados)

# Posição do valor da aceleração máxima
i = 0 
while lista_aceleracoes[i] != max(lista_aceleracoes):
    i += 1

# Aceleração máxima
acel_maxima = lista_aceleracoes[i]
tempo_minimo = math.sqrt((2*100)/acel_maxima)

# Atleta vencedor
for name, time in x.items():
    if time == tempo_minimo:
        print('O vencerdor é {0} com tempo de conclusão {1} s'.format(name, time))