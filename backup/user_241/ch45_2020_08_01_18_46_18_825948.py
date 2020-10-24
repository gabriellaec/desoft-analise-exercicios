x = int(input('Digite um número positivo: '))
lista = []
while x > 0:
        lista.append(x)
        x = int(input('Digite um número positivo: '))
        y = lista.reverse()    
        print(y)