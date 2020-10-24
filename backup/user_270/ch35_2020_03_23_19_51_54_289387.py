t = True
soma = 0
while t:
    per = int(input("Escreva um número: "))
    if  per == 0:
        t = False
    else:
        soma += per
print(soma)