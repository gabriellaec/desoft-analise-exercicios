a = 0
lista = []
while (a!=1):
    numero = int(input("Digite numeros inteiros: "))
    if numero > 0:
        lista.append(numero)
        print (lista)
    else: 
        for i in reversed(lista):
            print (i)
            a = 1