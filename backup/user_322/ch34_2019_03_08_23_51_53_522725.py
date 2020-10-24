deposito = int(input("Qual o valor do deposito:?"))
juros = int(input("Qual a taxa de juros:?"))       
i = 1
total = 0
while i < 25:
    valor_mes = deposito * (juros) ** i
    print(valor_mes)
    i = i + 1
    total = valor_mes - deposito
print(total)
    