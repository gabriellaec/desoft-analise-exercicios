duvida = True

while duvida == True:
    duvida = input ('tem duvida? ')
    if duvida == 'não':
        print ('Até a próxima')
        duvida = False
    else:
        print('Pratique mais')
        duvida = True