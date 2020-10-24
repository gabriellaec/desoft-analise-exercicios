salario=float(input("Qual é o salário bruto?"))
dependentes=int(input("Qual é o numero de dependentes"))
alq=0
if salario<=1045:
    INSS=salario*0.075
elif salario<=2089.60 and salario>=1045.01:
    INSS=salario*0.09
elif salario>=2089.61 and salario<=3134.40:
    INSS=salario*0.12
elif salario>=3134.41 and salario<=6101.06:
    INSS=salario*0.14
else:
    INSS=671.12
if alq<1:
    bc=salario-INSS-(dependentes*189.59)
else:
    bc=salario-alq-(dependentes*189.59)
if bc<=1903.98:
    alq2=0
    ded=0
elif bc>=1903.99 and bc<=2826.65:
    alq2=0.075
    ded=142.80
elif bc>=2826.66 and bc<=3751.05:
    alq2=0.15
    ded=354.80
elif bc>=3751.06 and bc<=4664.68:
    alq2=0.225
    ded=636.13
else:
    alq2=0.275
    ded=869.36
IRRF=(bc*alq2)-ded
print(IRRF)
    