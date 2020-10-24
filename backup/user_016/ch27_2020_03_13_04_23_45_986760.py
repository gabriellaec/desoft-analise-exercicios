tem_duvidas = True
while tem_duvidas:
    r = str(input('Tem alguma dúvida? '))
    if r != 'não':
        print('Pratique mais')
    else:
        tem_duvidas = False
print('Até a próxima')