tem_duvidas = True
while tem_duvidas:
    resposta = input('alguma duvida?(s/n) ')
    if  resposta != 'não':
        print ('Pratique mais')
    else:
        tem_duvidas = False
print ('Até a proxima')