salario = int(input("Qual o seu salário?: R$ "))
def salario_aumento(salario):
    if salario>1250:
        return "O seu salário final é R${0:.2f}".format(salario*1.1)
    elif salario<=1250:
        return "O seu salário final é R${0:.2f}".format(salario*1.15)