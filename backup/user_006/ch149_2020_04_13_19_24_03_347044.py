salario=int(input("Digite o salário"))
dependentes=int(input("Digite o número de dependentes"))

if salario<= 1045:
    inss=salario*0.075
elif salario<=2089.6:
    inss=salrio*0.09
elif salario<=3134.4:
    inss=salario*0.12
elif salario<=6101.06:
    inss=salario*0.14
else:
    inss=671.12

basedecalculo=salario-inss-dependentes*189.59

if basedecalculo<=1903.98:
    a=0
    d=0
elif basedecalculo<=2826.65:
    a=0.075
    d=142.8
elif basedecalculo<=3752.05:
    a=0.15
    d=354.8
elif basedecalculo<=4664.68
    a=0.225
    d=636.13
else:
    a=0.275
    d=869.36

irrf=basedecalculo*a-d
print(irrf)
