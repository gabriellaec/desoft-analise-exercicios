tem_duvidas = True
duvida = input('Você tem dúvida? (sim/não) ')

while tem_duvidas:
    if duvida != 'não':
        print('Pratique mais')
    else:
        tem_duvidas = False

print('Até a próxima')