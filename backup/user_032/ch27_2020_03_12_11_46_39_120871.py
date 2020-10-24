tem_duvidas = True
while tem_duvidas:
    pergunta = input('Você tem alguma dúvida?:')
    if pergunta != 'não':
        print('Pratique mais')
    else:
        tem_duvidas = False
print('Até a próxima')