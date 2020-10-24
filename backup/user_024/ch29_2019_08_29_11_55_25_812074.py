def calcula_aumento(salario):
    salario = int(input("Qual o seu salário atual?"))
    if salario > 1250:
        salario_novo = salario*1.1
    else:
        salario_novo = salario*1.15
    print(salario_novo)