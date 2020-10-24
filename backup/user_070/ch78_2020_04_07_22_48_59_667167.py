x = 0
dicio = {}
while x != 'sair':
    x = input('nome do atleta: ')
    if x != 'sair':
        y = float(input('aceleração: '))
        dicio[x] = y
def calcula_tempo(dicio):
    for atleta,a in dicio.items():
        dicio[atleta] = (200/a)**0.5
    return dicio
dicio = calcula_tempo(dicio)
mx = 0
for atleta,tempo in dicio.items():
    if tempo < mx or mx == 0:
        mx = tempo
        vencedor = atleta
print('O vencedor é {0} com tempo de conclusão de {1} s'.format(vencedor,mx))