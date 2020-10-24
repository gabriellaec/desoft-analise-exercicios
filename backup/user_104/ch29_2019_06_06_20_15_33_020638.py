salario = int(input('Qual é seu salário?'))
def calcula_aumento(salario):
    if salario > 1250:
        aumento = salario*(1/10)
    elif salario <= 1250:
        aumento = salario*(15*(1/100))
    return aumento
print(calcula_aumento(salario))                