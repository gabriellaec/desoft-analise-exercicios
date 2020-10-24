salario= float(input("Qual o seu salário bruto?: "))
num_dependentes= float(input("Qual seu número de dependentes?: "))

if salario<= 1045.00:
    aliq=0.075
    contrib= int(0.075*salario)
    
elif 1045.01<=salario<= 2089.60:
    aliq=0.09
    contrib= int(0.09 * salario)
    
elif salario>=2089.61 or salario<= 3134.40:
    aliq=0.12
    contrib= int(0.12 * salario)
    
elif 3134.41<=salario<=6101.06:
    aliq=0.14
    contrib= int(0.14 * salario)
    
elif salario>6101.06:
    aliq= 671.12
    contrib= 671.12
    
base_de_calc= int (salario - contrib - (num_dependentes*189.59))


if base_de_calc<=1903.98:
    aliq2=0.0
    ded= 0.00
    
elif 1903.99<=base_de_calc<=2826.65:
    aliq2=0.075
    ded=142.80
    
elif 2826.66<=base_de_calc<=3751.05:
    aliq2=0.15
    ded=354.80
    
elif 3751.06<=base_de_calc<=4664.68:
    aliq2=0.225
    ded=636.13
    
elif base_de_calc>4664.68:
    aliq2=0.275
    ded=869.36

IRRF = int((base_de_calc * aliq2) - ded )
print (IRRF)