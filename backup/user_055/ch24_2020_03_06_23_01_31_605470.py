def calcula_aumento(salario):
    salario = float(input())
    if salario > 1250:
        aumento = (salario*0.1)
    if salario < 1250 or salario == 1250:
        aumento  = (salario*0.15)