tem_duvidas = True

while tem_duvidas:
    resposta = input('Tem dúvidas? (sim/não): ')
    if resposta == 'não':
        print ('Até a próxima')
    else:
        tem_duvidas = False
        print ('Pratique mais')
        
print ('Até a próxima')