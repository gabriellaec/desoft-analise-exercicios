salario_bruto=int(input('Qual o seu salário bruto? '))
dependentes=int(input('Quantos dependentes você tem? '))

if salario_bruto<1045.00:	
    aliquota=0.075
    inss=aliquota*salario_bruto
elif 1045.01<salario_bruto<2089.60:
    aliquota=0.09
    inss=aliquota*salario_bruto
elif 2089.61<salario_bruto<3134.40:
    aliquota=0.12
    inss=aliquota*salario_bruto
elif 3134.41<salario_bruto<6101.06:
    aliquota=0.14
    inss=aliquota*salario_bruto
else:
    inss=671.12
    aliquota=100*inss/salario_bruto
    
base_de_calculo =salario_bruto-inss-dependentes*189.59  

if base_de_calculo<1903.98:
    aliquota=0
    dedução=0
    
elif 1903.99<base_de_calculo<2826.65:
    aliquota=0.075
    dedução=142.8
elif 2826.66<base_de_calculo<3751.05:
    aliquota=0.15
    dedução=354.8
elif 3751.06<base_de_calculo<4664.68:
    aliquota=0.225
    dedução=636.13
else:
    aliquota=0.275
    dedução=869.36

IRRF=base_de_calculo*aliquota-dedução
print(IRRF)