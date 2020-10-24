salario = float(input("Qual o valor do seu salário?: "))
def calcula_aumento(salario):
    if salario <= 1250.00:
        y= salario*(15/100)
        return y
    else:
        y= salario*(10/100)
        return y
