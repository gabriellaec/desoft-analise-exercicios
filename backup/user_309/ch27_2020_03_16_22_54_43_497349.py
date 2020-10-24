duvidas = True
while duvidas:
    tem_duvidas = input('Voce tem duvidas(sim/não): ')
    if tem_duvidas != 'não':
        print('Pratique mais')    
    else:
        duvidas = False
print('Até a próxima')