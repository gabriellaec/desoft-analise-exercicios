def calcula_irrf(sal,pax):
    if sal <= 1045:
        inss = 0.075 * sal
    elif 1045.01 <= sal <= 2089.60:
        inss = 0.09 * sal
    elif 2089.61 <= sal <= 3.134.40:
        inss = 0.12 * sal
    elif 3.134.40 <= sal <= 6.101.06:
        inss = 0.14 * sal
    else:
        inss = 671.12
    base = sal - inss - pax*189.59
    if base <= 1903.98:
        aliq = 0
        ded = 0
    elif 1903.99 <= base <= 2826.65:
        aliq = 0.075
        ded = 142.80
    elif 2826.66 <= base <= 3751.05:
        aliq = 0.15
        ded = 354.80
    elif 3751.06 <= base <= 4664.68:
        aliq = 0.225
        ded = 636.13
    else:
        aliq = 0.275
        ded = 86936
    irrf = base * aliq - ded
    return irrf
sal = int(input('Qual o seu salário bruto?'))
pax = int(input('Quantos dependentes?'))
print(calcula_irrf(sal,pax))