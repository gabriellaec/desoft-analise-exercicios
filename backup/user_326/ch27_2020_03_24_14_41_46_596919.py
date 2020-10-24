tem_duvidas = True
while tem_duvidas:
    alguma_duvida = input('Você tem alguma dúvida? ')
    if alguma_duvida == 'Não' or alguma_duvida == 'não' or alguma_duvida == 'Nao' or alguma_duvida == 'nao':
        tem_duvidas = False
        
    else:
        print('pratique mais.')
print ('Até a próxima')