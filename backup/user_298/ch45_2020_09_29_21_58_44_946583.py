lista = []
digitando = True   
while digitando:
    a = int(input("Digite um numero positivo não nulo: "))
    if a > 0:
        lista.append(a)
    else:
        digitando = False
lista.reverse()
print(lista)