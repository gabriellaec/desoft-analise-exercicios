def calcula_aumento(salario):
        if salario > 1250:
                return "Seu salário é com correção:{0:.2f}".format(float(salario*1.1))
           
        elif salario <= 1250:
                 return ("Seu salário é com correção:{0:.2f}".format(float(salario*1.15)))

a=1249
print(calcula_aumento(a))
        