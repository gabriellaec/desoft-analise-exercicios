import math
def calcula_tempo(atletas):
    resultado = {}
    for atleta in atletas:
        if not atleta in resultado:
            resultado[atleta] = math.sqrt(200/atletas[atleta])
    return resultado

atletas = {}
atleta = str(input('digite o nome de um atleta: '))
while atleta != 'sair':  
    if not atleta in atletas:
        atletas[atleta] = int(input('digite o valor de sua aceleração '))

tempos = calcula_tempo(atletas)
menor_tempo = 3600
vencedor = 'eu'
for atleta, tempo in tempos.items():
    if tempo < menor_tempo:
        menor_tempo = tempo
        vencedor = atleta
   
print('O vencedor é {0} com tempo de conclusão de {1} s'.format(vencedor,menor_tempo))