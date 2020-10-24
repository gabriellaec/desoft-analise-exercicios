lista_numero = [1]
while lista_numero[-1] != 0:
    n = int(input('Digite um números: '))
    lista_numero.append(n)
print((sum(lista_numero) - 1))
              