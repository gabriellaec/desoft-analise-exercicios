a=input('Está se movendo? (n/s) ')
if a=='s':
    b=input('Deveria se mover? (n/s) ')
    if b=='s':
        print('Sem problemas!')
    elif b=='n':
        print('Silver tape')
elif a=='n':
    c=input('Deveria estar parado? (n/s) ')
    if c=='s':
        print('Sem problemas!')
    elif c=='n':
        print('WD-40')