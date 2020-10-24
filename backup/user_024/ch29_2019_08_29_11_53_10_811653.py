def calcula_aumento(salário):
    salario = float(input("Qual o seu salário atual?"))
    if salario > 1250:
        salario_novo = salario*1.1
    else:
        salario_novo = salario*1.15
    print(salario_novo)