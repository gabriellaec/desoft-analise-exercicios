tem_duvidas = True
while tem_duvidas:
    resposta = input('Alguma dúvida? (s/n): ')
    if resposta != 'n':
        print('Pratique mais') 
    else:
        tem_duvidas = False
print('Até a próxima')