#pi.py
salario = float(input("Digite o valor de seu salario bruto:"))
numdedep = int(input("Digite o número de dependentes:"))

if salario < 1045:
    contr = 0.075*salario
elif salario < 2089.60:
    contr = 0.09*salario
elif salario < 3134.40:
    contr = 0.12*salario
elif salario < 6101.06:
    contr = 0.14*salario
else:
    contr = 671.12

base_de_calc = salario - contr - (numdedep*189,59)

if base_de_calc < 1903.98:
    ali = 0
    ded = 0
elif base_de_calc < 2826.65:
    ali = 0.075
    ded = 142.8
elif base_de_calc < 3751.05:
    ali = 0.15
    ded = 354.8
elif base_de_calc < 4.664.68:
    ali = 0.225
    ded = 636.13
else:
    ali = 0.275
    ded = 869.36

irrf = (base_de_calc*ali) - ded
print(irrf)