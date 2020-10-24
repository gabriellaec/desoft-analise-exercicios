number = int(input("Digite um número"))
lista = []
while number > 0:
    lista.append(number)
    number = int(input("Digite um número"))
    
lista.reverse()

print(lista)