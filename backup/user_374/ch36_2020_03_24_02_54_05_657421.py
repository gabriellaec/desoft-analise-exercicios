teste =  True
n = int(input("Digite um número "))
k = 1
calculo = 1
def fatorial(n):
    while teste:
        if n != k:
            calculo = calculo * k
            k = k + 1
            return calculo
        else:
            teste = False
            return calculo
        