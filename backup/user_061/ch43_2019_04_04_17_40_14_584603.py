def Collatz_par(numero):
    numero = numero/2
    return numero
def Collatz_impar(numero):
    numero = 3*numero + 1
    return numero
def Collatz(numero):
    n = 0
    while numero != 1:
        if numero % 2 == 0:
            numero = Collatz_par(numero)
        elif numero % 2 != 0:
            numero = Collatz_impar(numero)
        n += 1
    return n

maior = 0
for i in range(13):
    a = Collatz(i)
    if a > maior:
        maior = a
print(maior)