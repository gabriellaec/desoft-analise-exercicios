import math
salario_bruto=float(input('Qual o seu salário bruto?'))
n_dependentes=int(input('E quantos dependentes?'))
aliquota1=0
aliquota2=0
Deducao=0
valor_fixo=0
IRRF=0
if salario_bruto<=1045:
    aliquota1=0.075
elif salario_bruto>1045 and salario_bruto<=2089.60:
    aliquota1=0.09
elif salario_bruto<=3134.40 and salario_bruto>=2089.61:
    aliquota1=0.12
elif salario_bruto>=3134.41 and salario_bruto<=6101.06:
    aliquota1=0.14
else:
    aliquota1=0
    valor_fixo=671.12
base_cauculo=salario_bruto -(salario_bruto*aliquota1) - valor_fixo -(n_dependentes*189.59)
if base_cauculo<=1903.98:
    aliquota2=0
    Deducao=0
elif base_cauculo>=1903.99 and base_cauculo<=2826.65:
    aliquota2=0.075
    Deducao=142.8
elif base_cauculo>=2826.66 and base_cauculo<=3751.05:
    aliquota2=0.15
    Deducao=354.8
elif base_cauculo>=3751.06 and base_cauculo<=4664.68:
    aliquota2=0.225
    Deducao=636.13
elif base_cauculo>4664.68:
    aliquota2=0.275
    Deducao=869.36
IRRF=(base_cauculo*aliquota2)-Deducao
print('O seu IRRF é de R${0:.2f}'.format(IRRF))