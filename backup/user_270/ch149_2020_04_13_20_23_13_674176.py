sal= float(input("Qual o seu salário? "))
num = int(input("Qual o número de dependentes? "))

cotribu = 0
if sal <= 1045 :
    contribu = 0.075*sal
elif sal >= 1045.01 and sal <=2089.60  :
    contribu = 0.09*sal
elif sal >= 2089.61 and sal <= 3134.40:
    contribu = 0.12*sal
elif sal >= 3134.41 and sal <= 6101.06 :
    contribu = 0.14*sal
elif sal > 6101.06 :
    contribu = 671.12
    
base = sal - contribu - num*189.59

ali = 0
dedu = 0
if base <= 1903.98:
    ali = 0
    dedu = 0
elif base >= 1903.99 and base <= 2826.65 :
    ali = 0.075
    dedu = 142.80
elif base >= 2826.66 and base <= 3751.05 :
    ali = 0.15
    dedu = 354.80
elif base >= 3751.06 and base <= 4664.68 :
    ali = 0.225
    dedu = 636.13
elif base > 4664.68 :
    ali = 0.275
    dedu = 869.36
    
irrf = base * ali - dedu
print(irrf)