import math
def calcula_tempo(atletas):
    resultado = {}
    for atleta in atletas:
        if not atleta in resultado:
            resultado[atleta] = math.sqrt(200/atletas[atleta])
    return resultado

atletas = {}
atleta = str(input('digite o nome de um atleta: '))
if atleta != 'sair':  
    if not atleta in atletas:
        atletas[atleta] = int(input('digite o valor de sua aceleração '))

tempos = calcula_tempo(atletas)
for tempo in tempos.values():
    i = 0
    vencedor = {}
    vencedor[winner] = tempos[i]
    while i < len(tempos) - 1:
        if tempo[i+1] < tempo[i]:
            vencedor = tempos[i+1]
        else: 
            vencedor = tempos[i]
        i += 1
print('O vencedor é {0} com tempo de conclusão de {1} s'.format(vencedor.keys(),vencedor.values()))