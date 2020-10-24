inss=0
salario = float(input("Qual é o seu salario?:"))
dependentes = int(input("Qual o numero de dependentes seus?"))
if salario<= 1045.00:
    inss=salario*0.075
elif salario<= 2089.60:
    inss*0.09
elif salario<=3134.40:
    inss = salario*0.12
elif salario<= 6101.06:
    inss=salario*0.14
else:
    inss=671.12
base = salario-inss-(dependentes*189.59)
if base<=1903.98:
    a=0
    d=0
elif base<= 2826.65:
    a=0.075
    d=142.80
elif base<=3751.05:
    a=0.15
    d=354.80
elif base<= 4664.68:
    a =0.225
    d=636.13
else:
    a=0.275
    d=869.36

irrf=(base*a)-d
print(irrf)
                 