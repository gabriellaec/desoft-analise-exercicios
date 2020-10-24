tem_duvidas = True

while tem_duvidas:
     resposta = input('Você tem dúvidas? (Sim/Não) ')
     if  resposta != 'não':
         print('Pratique mais')
     else:
        tem_duvidas = False
        print ('Até a próxima')