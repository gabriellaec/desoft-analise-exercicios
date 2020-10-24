lista= []
n = int(input("Digite um numero inteiro:"))
while n > 0:
    lista.append(n)
    n = int(input("Digite um numero inteiro:"))
    
i = len(lista) - 1
while i >= 0:
    print(lista[i])
    i -=1