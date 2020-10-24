def quantos_uns(a):
    b = 0
    for i in a:
        if i == "1":
            b += 1
    return b
numero = input("coloque um número ")
print(quantos_uns(numero))
        