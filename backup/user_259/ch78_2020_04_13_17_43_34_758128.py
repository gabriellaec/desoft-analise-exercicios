from math import sqrt
run = True
corredores = {}
while run:
    nome = input('Corredor: ')
    if nome == 'sair':
        run = False
    else:
        aceleração = float(input('Aceleração: '))
        corredores[nome] = aceleração

def calcula_tempo(dic):
    tempos = {}
    for i in dic:
        tempo = sqrt(100/(dic[i]/2))
        tempos[i] = tempo
    max_tempo = 1e3
    vencedor = ''
    for i in tempos:
        if tempos[i]<max_tempo:
            max_tempo = tempos[i]
            vencedor = i
    return 'O vencedor é {0} com tempo de conclusão de {1} s'.format(vencedor, max_tempo)
print(calcula_tempo(corredores))
       