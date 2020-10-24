#s = at^2/2
#t = sqrt(200/a)

import math

def tempo(a):
    t = math.sqrt(200/a)
    return t

def calcula_tempo(dicionario):
    tempos = {}
    for atletas in dicionario:
        a = dicionario[atletas]
        t = tempo(a)
        tempos[atletas] = t
    return tempos

lista_nomes = []
lista_aceleracoes = []

verif = False

while not verif:
    nome_atleta = input("Qual o nome do atleta?")
    aceleracao_dele = int(input("Aceleração desse atleta é? "))
    if nome_atleta == "sair":
        verif = True
    else:
        lista_nomes.append(nome_atleta)
        lista_aceleracoes.append(aceleracao_dele)
        


dicionario = {}
for nome in range(len(lista_nomes)):
    dicionario[lista_nomes[nome]] = lista_aceleracoes[nome]

tempos = calcula_tempo(dicionario)

def tempo_vencedor(tempos):
    menor_tempo = 100
    for nomes,menor in tempos.items():
        if tempos[nomes] < menor_tempo:
            menor_tempo = tempos[nomes]
    return menor_tempo

def nome_vencedor(tempos):
    tempo_do_vencedor = tempo_vencedor(tempos)
    for pessoa in tempos.keys():
        if tempos[pessoa] == tempo_do_vencedor:
                return pessoa
        
print('O vencedor é {0} com tempo de conclusão de {1} s'.format((nome_vencedor(tempos)),(tempo_vencedor(tempos))))