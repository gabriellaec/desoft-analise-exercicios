salario_bruto= int(input("Qual é o seu salário bruto? "))
dependentes=int(input("Quantas pessoas dependem do salário? "))

if salario_bruto<= 1045:
    inss=salario_bruto*0.075
elif 1045.01 <= salario_bruto <=2089.60:
    inss=salario_bruto*0.09
elif 2089.61 <= salario_bruto <=3134.40:
    inss=salario_bruto*0.12
elif 3134.41 <= salario_bruto <=6101.06:
    inss=salario_bruto*0.14
else:
    inss=671.12

base_de_calculo=salario_bruto-inss-dependentes*159.59

if base_de_calculo <=1903.98:
    aliquota=0
    deducao=0
elif 1903.99<=base_de_calculo<=2826.65:
    aliquota=0.075
    deducao=142.80
elif 2826.66<= base_de_calculo<=3751.05:
    aliquota=0.15
    deducao=354.80
elif 3751.06<=base_de_calculo<= 4664.68:
    aliquota=0.225
    deducao=636.13
else:
    aliquota=0.275
    deducao=869.36

irrf=base_de_calculo*aliquota-deducao
print(irrf)