salario = float (input("Salário : "))
def calcula_aumento(salario) :
    if salario > 1250:
        c = salario*1.1
        print(c)
    else:
        b = salario*1.15
        print(b)
    
