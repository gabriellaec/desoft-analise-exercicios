salario=float(input('Qual o seu salário?'))
dep=int(input('Quantos dependentes você tem? '))

if salario < 1450:
    inss=salario*0.075
elif salario>1450.1 and salario<2089.6:
    inss=salario*0.09
elif salario>2089.61 and salario<3134.4:
    inss=salario*0.12
elif salario>3134.41 and salario<6101.06:
    inss=salario*0.14
else:
    inss=671.12

print(inss)

base=salario-inss-dep*189.59
print(base)

if base<1903.98:
    ali=0
    deducao=0
elif base>1903.99 and base<2826.65:
    ali=base*0.075
    deducao=142.8
elif base>2826.66 and base<3751.05:
    ali=base*0.15
    deducao=354.8
elif base>3751.06 and base<4664.68:
    ali=base*0.225
    deducao=636.13
else:
    ali=base*0.275
    deducao=869.36

irff=(base*ali)-deducao

print(irff)