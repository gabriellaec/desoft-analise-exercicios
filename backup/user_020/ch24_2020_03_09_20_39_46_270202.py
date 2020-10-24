salario = int(input("Qual o seu salário?"))
if salario > 1250:
    aumento = salario*(1.1)
elif salario <= 1250:
    aumento = salario*(1.15)