n = int(input("Digite o valor de n: "))

def fatorial(n):
    fatorial = 1
    i = 2
    while i <= n:
        fatorial = fatorial*i
        i+=1
    return fatorial
print(fatorial(n))