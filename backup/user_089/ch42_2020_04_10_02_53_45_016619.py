jogar = True


lista = []

while jogar == True:
    palavra = input("Escolha uma palavra:")
    if palavra == 'fim':
        print(lista)
        break
    if palavra != 'fim':
        if palavra[0] == 'a':
            lista.append(palavra)
        else:
            jogar = True