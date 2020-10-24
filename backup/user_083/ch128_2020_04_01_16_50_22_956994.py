a=str(input('Está se movendo (s ou n) : '))
if a=='s':
    b=str(input('Deveria estar se movendo (s ou n): '))
    if b=='s':
        print('Sem problemas.')
    elif b=='n':
        print('Silver Tape.')
else:
    if a=='n':
        c=str(input('Deveria estar parado (s ou n): '))
        if c=='s':
            print('Sem problemas')
        elif c=='n':
            print('WD-40')