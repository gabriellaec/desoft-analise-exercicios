sb = float(input('Qual o seu salário bruto? '))
dep = int(input('Qual o seu número de dependentes? '))

if sb <= 1045.00:
    inss = sb*0.075
if 1045.00 < sb <= 2089.60:
    inss = sb*0.09
if 2089.60 < sb <= 3134.40:
    inss = sb*0.12
if 3134.40 < sb <= 6101.06:
    inss = sb*0.14
if sb > 6101.06:
    inss = 671.12

bc = sb - inss - (dep*189.59)

if bc <= 1903.98:
    ali = 0.00
    ded = 0
if 1903.99 < bc <= 2826.65:
    ali = 0.075
    ded = 142.80
if 2826.65 < bc <= 3751.05:
    ali = 0.15
    ded = 354.80
if 3751.05 < bc <= 4664.68:
    ali = 0.225
    ded = 636.13
if bc > 4664.68:
    ali = 0.275
    ded = 869.36

irff = (bc*ali)-ded

print('O seu Imposto de Renda na Fonte (IRFF) é : {:.2f}'.format(irff))
