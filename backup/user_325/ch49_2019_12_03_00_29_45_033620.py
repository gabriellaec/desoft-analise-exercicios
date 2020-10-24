numeros_inteiros = int(input("num inteiro: "))
lista_num = []
while numeros_inteiros != 0 and numeros_inteiros > 0:
    lista_num.append(numeros_inteiros)
    numeros_inteiros = int(input("num inteiro: "))
print(lista_num[::-1])