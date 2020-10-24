temDuvidas = True

while temDuvidas == True:
    p = input('Voce tem duvidas?: ')
    if p != 'não':
        print("Pratique mais")
    else:
        print("Até a próxima")
        temDuvidas = False