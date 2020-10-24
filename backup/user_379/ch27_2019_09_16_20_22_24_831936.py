def funcao(a,b):
    tp = b * 10 * 365 * a # minuos
    return tp / (24 * 60)

b=int(input("digite quantos por dia"))
a=int(input("digite o tempo que você fuma em anos"))
print(funcao(a,b))