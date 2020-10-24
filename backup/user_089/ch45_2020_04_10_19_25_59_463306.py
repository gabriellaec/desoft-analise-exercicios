jogar = True

while jogar:
    numero = int(input("Digite um número"))
    lista = []
    if numero > 0:
        lista.append(numero)
        jogar = True
    else:
        lista.reverse()
        print(lista)