def calcula_aumento (salario):
    if salario>1250:
        return "O seu salário final é R${0:.2f}".format(salario*1.1)
    else:
        return "O seu salário final é R${0:.2f}".format(salario*1.15)
        
salario = float(input("Qual o seu salário atual?: R$ "))
print (calcula_aumento(salario))