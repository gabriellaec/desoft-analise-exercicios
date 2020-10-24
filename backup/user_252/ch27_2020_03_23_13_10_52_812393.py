tem_duvidas=True
while tem_duvidas:
    a=str(input('Voce tem alguma duvida?'))
    if a=='não':
        tem_duvidas=False
        print('legal')
    elif a!='não':
        print('Pratique mais')