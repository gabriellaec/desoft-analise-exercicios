def calcula_salario(salario):
        salario=int(input("Qual seu salário? "))
        if salario > 1250:
                print("Com o ajuste seu salário é R${0:.2f}".format(float(salario*1.1)))
        else:
                print("Com o ajuste seu salário é R${0:.2f}".format(float(salario*1.15))) R${0:.2f}".format(float(1.15*salario))
