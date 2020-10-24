salario = float(input("Qual o seu salário bruto? "))
dependentes = int(input("Quantos dependentes você tem? "))

if salario <= 1045.00:
    inss = 0.075*salario
elif salario >= 1045.01 and salario <= 2089.60:
    inss = 0.09*salario
elif salario >= 2089.61 and salario <= 3134.40:
    inss = 0.12*salario
elif salario >= 3134.41 and salario <= 6101.06:
    inss = 0.14*salario
else:
    inss = 671.12
    
base = salario - inss - dependentes*189.59

if base <= 1903.98:
    aliquota = 0.0
    deducao = 0.0
elif base >= 1903.99 and base <= 2826.65:
    aliquota = 0.075
    deducao = 142.80
elif base >= 2826.66 and base <= 3751.05:
    aliquota = 0.15
    deducao = 354.80
elif base >= 3751.06 and base <= 4664.68:
    aliquota = 0.225
    deducao = 636.13
else:
    aliquota = 0.275
    deducao = 869.36

irrf = base*aliquota - deducao

print("O valor do seu irrf é de {0}".format(irrf))