resposta = input('O objeto está se movendo?
s ou n? ')
if resposta == 's':
    resposta1 = input('Deveria se mover?
s ou n? ')
    if resposta1 == 's':
        print('Sem problemas!')
    else:
        print('Silver tape')
else:
    resposta2 = input('Deveria estar parado?
s ou n? ')
    if resposta2 == 's':
        print('Sem problemas!')
    else:
        print('WD-40')