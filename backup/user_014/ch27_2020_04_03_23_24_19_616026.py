tem_duvidas = True
duvida = input('Você tem dúvida? (sim/não) ')

while tem_duvidas:
    duvida = input('Você tem dúvida? (sim/não) ')
    if duvida != 'não':
        print('Pratique mais')
    else:
        tem_duvidas = False

print('Até a próxima')