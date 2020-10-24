tem_duvidas = True
while tem_duvidas:
    resposta = input('Tem alguma dúvida? ')
    if resposta != 'não':
        print('Pratique mais')
    else:
        tem_duvidas = False
print('Até a próxima')