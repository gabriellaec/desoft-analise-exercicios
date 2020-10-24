tem_duvidas=True
while tem_duvidas:
    a=str(input('Voce tem alguma duvida?'))
    if a=='não':
        tem_duvidas=False
        print('Até a próxima')
    elif a!='não':
        print('Pratique mais')