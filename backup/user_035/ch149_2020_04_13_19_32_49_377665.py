sal_bruto = float(input("Qual é o seu salário bruto? "))
dependentes = int(input("Quantos dependendes? "))
if sal_bruto <= 1045:
    bdc = sal_bruto - (sal_bruto*0.075) - dependentes * 189.59
elif sal_bruto >= 1045.01 and sal_bruto <= 2089.60:
    bdc = sal_bruto - (sal_bruto*0.09) - dependentes * 189.59
elif sal_bruto >= 2089.61 and sal_bruto <= 3134.40:
    bdc = sal_bruto - (sal_bruto*0.12) - dependentes * 189.59
elif sal_bruto >= 3134.41 and sal_bruto <= 6101.06:
    bdc = sal_bruto - (sal_bruto*0.14) - dependentes * 189.59
else:
    bdc = sal_bruto - 671.12 - dependentes * 189.59


if bdc <= 1903.98:
    IRRF = bdc * 0 - 0
elif bdc >= 1903.99 and bdc <= 2826.65:
    IRRF = bdc * 0.075 - 142.80
elif bdc >= 2826.66 and bdc <= 3751.05:
    IRRF = bdc * 0.15 - 354.80
elif bdc >= 3751.06 and bdc <= 4664.68:
    IRRF = bdc * 0.225 - 636.13
else:
    IRRF = bdc * 0.275 - 869.36
print IRRF