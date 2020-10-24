def calcula_aumento(int(salario)):
        if salario > 1250:
                return "Seu salário é com correção:R${0:.2f}".format(float(salario*1.10))
           
        elif salario <= 1250:
                 return "Seu salário é com correção:R${0:.2f}".format(float(salario*1.15))


        
       