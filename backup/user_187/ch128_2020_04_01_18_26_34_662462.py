A = True
while A:
    a = input('Está se movendo(s/n)?: ')
    if a == 'n':
        B=True
        while B:
            b=input('Deveria estar parado(s/n)?: ')
            if b =='s':
                print('Sem problemas!')
            elif b =='n':
                print('WD-40')
            else:
                B=False
    elif a=='s':
        C=True
        while C:
            c=input('Deveria se mover(s/n)?: ')
            if c=='s':
                print('Sem Problemas!')
            elif c=='n':
                print('Silver Tape')
            else:
                C=False
    else:
        A=False
