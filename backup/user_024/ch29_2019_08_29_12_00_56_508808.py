def calcula_aumento(salario):
    salario = float(input("Qual o seu salário atual?"))
    if salario > 1250:
        salarionovo = salario*1.1
    else:
        salarionovo = salario*1.15
    print(salarionovo)
