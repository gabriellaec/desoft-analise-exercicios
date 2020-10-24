lista = []
n = int(input('Digite um número: '))

while n>0:
    n = int(input('Digite um número: '))
    lista.append(n)
    
print(lista.sort(reverse=True))