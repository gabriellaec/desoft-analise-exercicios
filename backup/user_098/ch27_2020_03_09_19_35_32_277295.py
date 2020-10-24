tem_duvidas = True

while tem_duvidas: 
    resp = input("Vc tem duvida mah? ")
    if resp != 'não':
        print('Pratique mais')
    else:
        tem_duvidas = False
        print("Até a próxima")