lista = []
numero = int(input("Digite numeros inteiros positivos: "))

while numero != 0 or numero < 0:
    lista.append(numero)
    numero = int(input("Digite numeros inteiros positivos: "))
    
print(lista[::-1])
    
