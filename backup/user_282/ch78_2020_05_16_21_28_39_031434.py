def calcula_tempo(acc):
    import math as m
    t = dict()
    for n, a in acc.items():
        t[n] = m.sqrt(200/a)
    return t

loop = True
nome = ''
acc = dict()
while loop:
        nome = input('qual eh o nome do atleta? ')
        if nome == 'sair':
            loop = False
            break
        aceleracao = int(input('qual sua aceleracao? '))
        acc[nome] = aceleracao

tempo = list(calcula_tempo(acc).values())
x = min(tempo)
for n, t in calcula_tempo(acc).items():
    if t == x:
        print('O vencedor é {0} com tempo de conclusão de {1} s'.format(n, t))
