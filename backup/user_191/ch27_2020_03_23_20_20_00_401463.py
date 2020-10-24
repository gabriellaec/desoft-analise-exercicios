tem_duvidas = True
a=input('Duvidas?')
i=1
while tem_duvidas:
    if tem_duvidas:
        if a!='não':
            print('Pratique mais')
            a=input('Duvidas?')
            i=i+1
        else:
            print('Até a próxima')
            tem_duvidas = False