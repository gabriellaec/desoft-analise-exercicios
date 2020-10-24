sal = float(input("insira seu salário "))
def calcula_aumento(sal):
    if sal>1250:
        aumento1 = sal*0.1 + sal
        return aumento1
    elif sal<=1250:
        aumento1 = sal*0.15 + sal
        return aumento1

