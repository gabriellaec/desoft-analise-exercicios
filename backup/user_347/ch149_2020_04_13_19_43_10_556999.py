bruto = float(input("Qual o seu salário bruto?"))

if bruto <= 1045.00:
    a = 0.075
    inss = bruto * a
elif bruto<= 2089.60:
    a = 0.09
    inss = bruto * a
elif bruto <= 3134.40:
    a = 0.12
    inss = bruto * a
elif bruto <= 6101.06:
    a = 0.14
    inss = bruto * a
else:
    inss =  671.12

dep = int(input("Quantos dependentes?"))

base = bruto - inss - (dep*189.59)

if base <= 1903.98:
    ali = 0
    ded = 0
    irrf = (base*ali) - ded
elif base <= 2826.65:	
    ali = 0.075
    ded = 142.80
    irrf = (base*ali) - ded
elif base <= 3751.05:
    ali = 0.15
    ded = 354.80
    irrf = (base*ali) - ded
elif base <= 4664.68:
    ali = 0.225
    ded = 636.13
    irrf = (base*ali) - ded
else:
    ali = 0.275
    ded = 869.36
    irrf = (base*ali) - ded

print("O IRRF é {0}".format(irrf))