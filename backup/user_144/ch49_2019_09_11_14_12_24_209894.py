lista = []
numero = float(input("Digite numeros inteiros positivos: "))

while numero != 0 or numero < 0:
    lista.append(numero)
    numero = float(input("Digite numeros inteiros positivos: "))
    
print(lista[::-1])
    
