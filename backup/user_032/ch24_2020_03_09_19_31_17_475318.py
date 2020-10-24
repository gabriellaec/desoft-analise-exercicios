def calcula_aumento(salario):
    salario = float(input('Qual o seu salário?'))
    if salario > 1250:
        valor_aumento = int(salario) * 10/100
        return valor_aumento
    elif salario <= 1250:
        valor_aumento = int(salario) * 15/100