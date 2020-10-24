jogar = True


lista = []

while jogar == True:
    palavra = input("Escolha uma palavra:")
    if palavra == 'fim':
        n = 0
        for n in len(lista):
            print(lista[n])
           
        else: 
            break
    if palavra != 'fim':
        if palavra[0] == 'a':
            lista.append(palavra)
            
        else:
            jogar = True