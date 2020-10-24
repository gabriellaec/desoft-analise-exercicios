def salario_aumento(salario):
    if salario>1250:
        return salario*1.1
    elif salario<=1250:
        return salario*1.15
    
    
salario= float(input("Qual o seu salário?: R$ "))