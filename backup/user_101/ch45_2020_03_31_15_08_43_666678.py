num = int(input('Digite um número: '))
lista = []
while num > 0:
    lista.append(num)
    num = int(input('Digite um número: '))
    
while len(lista) > 0:
    print(lista[-1])
    del lista[-1]