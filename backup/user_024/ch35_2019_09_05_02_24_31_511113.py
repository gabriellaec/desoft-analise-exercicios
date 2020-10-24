inicial = float(input("Qual o depósito inicial? "))
taxa = float(input("Qual a taxa de juros da poupanca? "))
mensal=float(input("Qual o deposito mensal?"))
n=0
valor=0


while n<=24:
    valor=inicial*(1+taxa/100)
    print(valor)
    inicial=valor+mensal
    n = n + 1