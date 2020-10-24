salario=float(input("salario bruto: "))
dependentes=int(input("numero de dependentes?: ")) 
if salario<=1045:
    c=salario*0.075
elif salario>1045 and salario<=2089.60:
    c=salario*0.09
elif salario>2089.60 and salario<=3134.40:
    c=salario*0.12
elif salario>3134.40 and salario<=6101.06:
    c=salario*0.14
elif salario>6101.06:
    c=671.12
    
base=salario-c-(dependentes*189.59)

if base<=1903.98:
    d=0
    a=0
elif base>1903.98 and base<=2826.65:
    d=142.8
    a=0.075
elif base>2826.65 and base<=3751.05:
    d=354.8
    a=0.15
elif base>3751.05 and base<=4664.68:
    d=636.13
    a=0.225
else:
    d=869.36
    a=0.275

irrf=(base*a)-d
print (irrf)