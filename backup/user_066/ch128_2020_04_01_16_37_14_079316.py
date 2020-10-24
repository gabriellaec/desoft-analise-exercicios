movendo = input('Está se movendo? (s/n) ')
if movendo == 'n':
    deveria = input(' Deveria estar parado? (s/n) ')
    if deveria == 's':
        print('Sem problemas!')
    else:
        print('WD-40')
else:
    deveria = input('Deveria se mover ? (s/n)')
    if deveria == 'n':
        print('Silver tape')
    else:
        print('Sem problemas!')