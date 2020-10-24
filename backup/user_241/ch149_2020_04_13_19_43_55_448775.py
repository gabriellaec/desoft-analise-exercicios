p1 = float(input('Qual o seu salário ? '))
p2 = int(input(' quantas pessoas são dependentes desse salário ? '))
inss=0
if p1 <= 1045:
    inss += p1*0.075
if 2089.60 <= p1 > 1045:
    inss += p1*0.09 
if 2089.61 <= p1 <= 3134.40:
    inss += p1*0.12
if 3134.41 <= p1 <= 6101.06:
    inss += p1*0.14
if p1 > 6101.06:
    inss += 671.12
bdc = p1 - inss - p2*189.59
if bdc <= 1903.98:
    irrf = 0
if 1903.98 < bdc <= 2826.65:
    irrf = bdc*0.075-142.80
if 2826.65 < bdc <= 3751.05:
    irrf = bdc*0.15-354.80
if 3751.05 < bdc <= 4664.68:
    irrf = bdc*0.225-636.13
if bdc >4664.68:
    irrf = bdc*0.275-869.36
print('O seu IRRF é {0}'.format(irrf))