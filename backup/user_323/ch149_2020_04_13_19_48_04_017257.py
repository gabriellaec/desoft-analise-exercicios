s = float(input("Qual é o seu salario bruto?"))
d=int(input("Qual o seu número de dependentes?"))
if s <= 1045.00:
    INSS=s*0.075
elif s <=2089.60:
    INSS=s*0.09
elif s <=3134.40:
    INSS=s*0.12
elif s<=6101.06:
    INSS=s*0.14
else:
    INSS=671.12
x=s-INSS-(d*189.59)
if x<=1903.98:
    a=0
    y=0
elif x<=2826.65:
    a=0.075
    y=142.80
elif x<=3751.05:
    a=0.15
    y=354.80
elif x<=4664.68:
    a=0.225
    y=636.13
else:
    a=0.275
    y=869.36
IRRF=(x*a)-y
print(IRRF)