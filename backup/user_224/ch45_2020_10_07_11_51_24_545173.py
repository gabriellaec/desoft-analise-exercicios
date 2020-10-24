numeros_positivos = int(input('Digite numero inteiro positivo '))
lista = []
while numeros_positivos > 0 :
    lista.append(numeros_positivos)
    numeros_positivos = int(input('Digite outro numero '))

lista.reverse()

print(lista)
