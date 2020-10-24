#Exercício 77
import math

def calcula_tempo(atletas):
    tempos = {}
    for nome, aceleracao in atletas.items():
        t = math.sqrt(200/aceleracao)
        tempos[nome] = t
    return tempos
    
print(calcula_tempo({'Beatriz': 100}))

#Exercício 78
sair = True

while sair:
    atleta = input('Digite o nome de um atleta: ')
    if atleta == 'sair':
        sair = False
    else:
        a = float(input('Digite a aceleração de um atleta: '))
        calcula_tempo(atleta)
        tempo_vencedor = 0
        for nome,tempo in atleta.items():
            if tempo < tempo_vencedor:
                tempo_vencedor = tempo
    print('O vencedor é {0} com o tempo de {1}'.format(atleta.keys(), tempo_vencedor))
    sair = False