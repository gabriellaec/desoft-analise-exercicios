a = True
lista = []
while a:
    numero = int(input("Digite um número"))
    if numero != 0:
        lista.append(numero)
    else:
        a = False
print(sum(lista))