tem_duvidas = True
while tem_duvidas:
    resposta = input('voce tem duvidas?')
    if resposta != 'não':
        print('Pratique mais')
    else:
        print('Até a próxima')
        tem_duvidas = False