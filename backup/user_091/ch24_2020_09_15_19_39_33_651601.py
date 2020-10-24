def calcula_aumento(salario):
        if salario > 1250:
                return "Seu salário é com correção:R${0:.2f}".format(float(salario*1.10))
           
        elif salario <= 1250:
                 return ("Seu salário é com correção:R${0:.2f}".format(float(salario*1.15)))

a=1250.45
print(calcula_aumento(a))
        
       