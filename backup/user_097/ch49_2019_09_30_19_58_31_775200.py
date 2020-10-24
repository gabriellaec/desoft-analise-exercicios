numero = int(input("Digite um número: "))
listaNumeros = []
while(numero>0):
    listaNumeros.append(numero)
    numero = int(input("Digite um número: "))
listaInvertida = []
i = len(listaNumeros)
while(i>0):
    listaInvertida.append(listaNumeros[i-1])
    i = i - 1
print(listaInvertida)