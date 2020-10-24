n = int(input("Digite um número inteiro: "))
cont = 0
i = 0

while i <= n or cont < 2:
    i += 1
    x = n % i
    if x == 0:
        cont += 1
if cont <= 2:
        print("True")
else:
    print("False")