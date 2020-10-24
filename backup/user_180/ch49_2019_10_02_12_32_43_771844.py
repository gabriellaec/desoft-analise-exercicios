lista_numeros = []
numeros_inteiros = int(input("Me fale numeros inteiros positivos: "))
lista_numeros.append(numeros_inteiros)
while numeros_inteiros != 0 and numeros_inteiros > 0:
    numeros_inteiros = int(input("Me fale numeros inteiros positivos: "))
    lista_numeros.append(numeros_inteiros)
print(lista_numeros[::-1])