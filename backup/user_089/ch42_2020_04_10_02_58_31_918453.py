jogar = True


lista = []
n = 0
while jogar == True:
    palavra = input("Escolha uma palavra:")
    if palavra == 'fim':
        while n in len(lista):
            print(lista[n])
            n = n +1
        break
    if palavra != 'fim':
        if palavra[0] == 'a':
            lista.append(palavra)
            
        else:
            jogar = True