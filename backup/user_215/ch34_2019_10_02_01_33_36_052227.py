deposito_inicial = float(input("Qual foi o deposito inicial? "))
poupanca = float(input("Qual a taxa de juros da poupanca? "))
mes = 0
total = 0
while mes < 24:
    mensal = (mes * poupanca) * deposito_inicial
    print(mensal)
    total = ((mes * poupanca) * deposito_inicial) - deposito_inicial
    mes += 1
print(f(total):.2f)
    