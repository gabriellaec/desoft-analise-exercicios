def calcula_tempo (atletas):
    tempo = {}
    for nome, a in atletas.items():
        t = (200/a)**(1/2)
        tempo[nome] = t
    return tempo


vencedor = 1000
programa = True
while programa:
    NOME = input('Digite o nome: ')
    if NOME != 'sair':
        ACELERAÇÃO = float(input('Digite a aceleração: '))
        TEMPO = calcula_tempo (atletas)
        if TEMPO < vencedor:
            vencedor = TEMPO
            programa = True
    else:
        programa = False
if programa = False:
    print('O vencedor é {0} com tempo de conclusão de {1} s'.format(NOME, TEMPO))
                             