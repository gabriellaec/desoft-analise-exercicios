num = int(input("Numeros"))
soma = 0
while num != 0:
    soma += num
    num = int(input("Numeros"))
    if num == 0:
        break
print(soma)