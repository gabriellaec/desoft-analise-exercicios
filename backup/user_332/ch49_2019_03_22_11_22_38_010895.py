lista = []
numero = int(input("Numero "))


while (numero > 0):
    lista.append(numero)
    numero = int(input("Outro numero "))
    


print(lista[::-1])