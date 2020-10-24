sim = ['s','SIM','sim','Sim','S']
nao = ['n','NAO','nao','Nao','N']

se_movendo = input('Esta movendo? ')
if se_movendo in sim:
    mover = input('Deveria estar se movendo? ')
    if mover in sim:
        print('Sem problemas!')
    elif mover in nao:
        print('Silver tape')
    else:
        print('resposta invalida, algo na resposta esta errado!')
if se_movendo in nao:
    esta_parado = input('Deveria estar parado?')
    if esta_parado in sim:
        print('Sem problemas!')
    elif esta_parado in nao:
        print('Usar WD-40')
    else:
        print('resposta invalida, algo na resposta esta errado!')


        