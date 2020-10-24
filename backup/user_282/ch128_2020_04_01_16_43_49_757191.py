resposta = input('Está se movendo? ')
if resposta == 's':
    resposta1 = input('Deveria se mover? ')
    if resposta1 == 's':
        print('Sem problemas!')
    else:
        print('Silver tape')
else:
    resposta2 = input('Deveria estar parado? ')
    if resposta2 == 's':
        print('Sem problemas!')
    else:
        print('WD-40')