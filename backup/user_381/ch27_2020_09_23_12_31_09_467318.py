tem_duvidas = True

while tem_duvidas:
    resposta = input('Você tem dúvidas?: ')
    if resposta == 'não':
        print('Até a próxima!')
        tem_duvidas = False
    else:
        print('Pratique mais!')