tem_duvida=True
duvida=input('Tem dúvida: ')
while tem_duvida:
    if duvida == 'não':
        tem_duvida=False
        print('Até a próxima')
    else:
        print('Pratique mais')