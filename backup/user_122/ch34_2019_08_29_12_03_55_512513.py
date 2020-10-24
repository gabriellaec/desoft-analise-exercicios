dep_inicial = input(float("Qual o depósito inicial?"))
juros_anual = input(float("Qual a taxa de juros anual da poupança em porcentagem?"))

juros_mensal = (1 + juros_anual) ** (1/12) - 1

n = 0

while n <= 24:
    n += 1
    total = dep_inicial * (1 + juros_mensal) ** n
    print(total)