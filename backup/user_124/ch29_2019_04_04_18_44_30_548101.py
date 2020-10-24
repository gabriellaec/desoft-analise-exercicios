a = int(input("qual o salário do funcionário? : "))
def calcula_aumento(x):
        if a <= 1250:
            x = a * float(0.15)
        else:
            x = a * float(0.1)
        return x
            
        