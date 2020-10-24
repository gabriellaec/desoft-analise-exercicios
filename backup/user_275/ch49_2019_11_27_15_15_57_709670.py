numero = int(input('Digite numero inteiro positivo: '))
lista = []
while True:
    if numero > 0:
        lista.append(numero)
        numero = int(input('Digite numero inteiro positivo: '))
    else:   
        print(lista)
        break