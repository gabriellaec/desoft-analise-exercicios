a = input('Está se movendo? ')
if a == 'n':
    b = input('Deveria estar parado? ')
    if b == 'n':
        print('WD-40')
    elif b == 's':
        print('Sem problemas!')
elif a == 's':
    b = input('Deveria se mover? ')
    if b == 'n':
        print('Silver tape')
    elif b == 's':
        print('Sem problemas!')
