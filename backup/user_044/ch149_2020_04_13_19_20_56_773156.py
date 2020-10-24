sal=input("Qual é o seu salário bruto? ")
dep=int(input('Qual o seu número de dependentes? '))
cont=0
if sal<=1045.00:
    cont=sal*0.075
elif 1045.01<=sal<=2089.60:
    cont=sal*0.09
elif 2089.61<=sal<=3134.40:
    cont=sal*0.12
elif 3134.41<=sal<=6101.06:
    cont=sal*0.14
elif sal>6101.06:
    cont=671.12
base=sal-cont-(dep*189.59)
ali=0
ded=0
if base<=1903.98:
    ali=0
    ded=0
elif 1903.99<=base<=2826.65:
    ali=0.075
    ded=142.80
elif 2826.66<=base<=3751.05:
    ali=0.15
    ded=354.80
elif 3751.06<=base<=4664.68:
    ali=0.225
    ded=636.13
elif base>4664.68:
    ali=0.275
    ded=869.36
IRRF=(base*ali)-ded
print(IRRF)