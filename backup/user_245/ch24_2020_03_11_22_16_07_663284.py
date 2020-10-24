#sal = float(input("insira seu salário "))
def calcula_aumento(sal):
    if sal>1250.00:
        aumento1 = sal*0.1
        return aumento1
    elif sal<=1250.00:
        aumento1 = sal*0.15
        return aumento1