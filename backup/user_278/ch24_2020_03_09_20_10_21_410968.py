def salario_aumento(salario):
    if salario>1250:
        return "O seu salário final é R${0:.2f}".format(salario*1.1)
    elif salario<=1250:
        return "O seu salário final é R${0:.2f}".format(salario*1.15)
        
salario = float(input("Qual o seu salário?: R$ "))
print (salario_aumento(salario))