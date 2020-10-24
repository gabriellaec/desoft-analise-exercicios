num = int(input("Numeros"))
soma = 0
while num != 0:
    num = int(input("Numeros"))
    soma += num
    if num == 0:
        break
print(soma)