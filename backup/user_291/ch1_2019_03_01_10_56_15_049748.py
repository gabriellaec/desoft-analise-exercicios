def calcula_valor_devido(valor_emprestado, meses, juros):
    y = valor_emprestado*(1 + juros)**meses
    return y
a = int(input("Qual é o valor emprestado?: "))
b = int(input("Por quantos meses?: "))
c = int(input("Taxa de juros?: "))

x = calcula_valor_devido(a, b, c)

print(x)
