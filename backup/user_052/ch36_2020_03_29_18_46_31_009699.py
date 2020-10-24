def fatorial (n):
    total = 1
    while n > 0:
        total = total * n
        n += -1
    return total
x = int(input("Qual número voce deseja calcular o fatorial?"))
print (fatorial(x))