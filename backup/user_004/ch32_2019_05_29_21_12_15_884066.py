duvida = True
while duvida:
    pergunta=str(input('Você tem dúvidas? '))
    if pergunta == 'sim' or pergunta == 'Sim':
        print('Pratique mais')
    else:
        print('Até a próxima')
        duvida = False
                 