tem_duvida=True
while tem_duvida:
    duvida=input('Tem dúvida: ')
    if duvida == 'não':
        tem_duvida=False
        print('Até a próxima')
    else:
        print('Pratique mais')