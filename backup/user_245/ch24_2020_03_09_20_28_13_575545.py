sal = int(input("insira seu salário"))
def aumento(sal):
    if sal>1250:
        sal = sal*0.1 + sal
        print (sal)
    elif sal<=1250:
        sal = sal*0.15 + sal
