p = str(input('Está se movendo? '))
if p == 's':
    p1 = str(input('Deveria se mover? '))
    if p1 == 's':
        print('Sem problemas!')
    elif p1 == 'n':
        print('Silver tape')
elif p == 'n':
    p2 = str(input('Deveria estar parado? '))
    if p2 == 's':
        print('Sem problemas!')
    elif p2 == 'n':
        print('WD-40')