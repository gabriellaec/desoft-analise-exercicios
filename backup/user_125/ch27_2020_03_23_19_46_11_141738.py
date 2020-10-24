tem_duvidas=True 
input ('voce tem dúvidas ') 
while tem_duvidas: 
    a=input('você tem dúvidas? ')
        if a!='não':
            print ('Pratique mais')
        elif a=='não':
            tem_duvidas = False
            print('Até a próxima')