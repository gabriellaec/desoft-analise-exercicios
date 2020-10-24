import math
def calcula_tempo(dic_atletas):
    tempos = {}
    for atletas in dic_atletas:
        tempo = math.sqrt(200/dic_atletas[atletas])
        tempos[atletas] = tempo
    return tempos
dic_atletas = {}
nome = input("Nome do atleta: ")
aceleracao = float(input("Aceleração: "))
dic_atletas[nome] = aceleracao
while nome != 'sair':
    nome = input("Nome do atleta: ")
    if nome != 'sair':
        aceleracao = float(input("Aceleração: "))
        dic_atletas[nome] = aceleracao
        
vencedor = ''
tempo_minimo = 9999999999999999999999999

for atleta in calcula_tempo(dic_atletas):
    if calcula_tempo(dic_atletas)[atleta] < tempo_minimo:
        tempo_minimo = calcula_tempo(dic_atletas)[atleta]
        vencedor =  atleta
print ('O vencedor é {0} com tempo de conclusão de {1} s'.format(vencedor,tempo_minimo))