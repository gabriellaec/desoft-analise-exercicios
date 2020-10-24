a=float(input("salario bruto:"))
b=int(input("numero de dependentes:"))
if a <= 1045:
    l=0.075
    x= a*l
elif a > 1045 and a <= 2089.6:
    l=0.09
    x= a*l
elif a > 2089.6 and a <= 3134.4:
    l=0.12
    x =a*l
elif a > 3134.40 and a <=6101.06:
    l=0.14
    x= a*l
else:
    x =671.12
    
base_calculo= a - x - b*189.59

if x <= 1903.98:
    al=0
    deducao=0
elif x > 1903.98 and x <= 2826.65:
    al=0.075
    deducao=142.80
elif x >2826.65 and x <=3751.05:
    al=0.15
    deducao=354.80
elif x > 3751.05 and x <=4664.68:
    al=0.225 
    deducao=636.13
else:
    al=0.275
    deducao=869.36
irrf=base_calculo*al-deducao
print("seu imposto e{}".format(irrf))