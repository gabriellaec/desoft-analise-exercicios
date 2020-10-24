jogar = True
lista = []
while jogar:
    numero = int(input("Digite um número"))
    
    if numero > 0:
        lista.append(numero)
        jogar = True
    
    else:
        lista.reverse()
        print(lista)
        jogar = False