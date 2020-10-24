inicial = float(input("Qual o depósito inicial? "))
taxa = float(input("Qual a taxa de juros da poupanca? "))
n=0
valor=0


while n<=24:
    inicial=inicial+valor
    valor=inicial*(1+taxa/100)
    print(valor)
    n = n + 1