from math import sqrt

def calcula_tempo(atletas):
    tempo_de_conclusao = {}
    for nome in atletas:
        tempo_atleta = sqrt(200 / atletas[nome]) 
        tempo_de_conclusao[nome] = tempo_atleta
    return tempo_de_conclusao

def atleta_mais_rapido(dicionario):
    tempo_vencedor = tempo_mais_curto(dicionario)
    for nome in dicionario.keys():
        if dicionario[nome] == tempo_vencedor:
            return nome

def tempo_mais_curto(dicionario):
    menor_tempo = 2000
    for nome in dicionario.keys():
        if menor_tempo > dicionario[nome]:
            menor_tempo = dicionario[nome]
    return menor_tempo

nomes_aceleracoes_atletas = {}
sair =  False
while not sair:
    nome = input("Digite o nome do atleta: ")
    if nome == "sair":
        sair = True
    else:
        aceleracao = float(input("Digite a aceleracao do atleta: "))
        nomes_aceleracoes_atletas[nome] = aceleracao
        
nomes_tempos_atletas = calcula_tempo(nomes_aceleracoes_atletas)

nome = atleta_mais_rapido(nomes_tempos_atletas)

tempo = tempo_mais_curto(nomes_tempos_atletas)

print('O vencedor é {0} com tempo de conclusão de {1} s'.format(nome, tempo))