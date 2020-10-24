import math
def calcula_tempo(dic_atletas):
    tempos = {}
    for atletas in dic_atletas:
        tempo = math.sqrt(200/dic_atletas[atletas])
        tempos[atletas] = tempo
    return tempos
dic_atletas = {}
nome = input("Nome do atleta: ")
aceleracao = input("Aceleração: ")
dic_ateltas[nome] = aceleracao
while nome != 'sair':
    nome = input("Nome do atleta: ")
    if nome != 'sair':
        aceleracao = input("Aceleração: ")
        dic_ateltas[nome] = aceleracao
    
vencedor = ''
tempo_minimo = 0

for atleta in tempo:
    if tempo[atleta] > tempo_minimo:
        tempo_minimo = tempo[atleta]
        vencedor =  alteta
print ('O vencedor é {0} com tempo de conclusão de {1} s'.format(vencedor,tempo_minimo)
