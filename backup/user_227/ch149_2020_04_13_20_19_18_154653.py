salario_bruto=float(input("Qual o seu salário bruto? "))
numero_dependentes=int(input("Qual o seu número de dependentes? "))

if salario_bruto<=1.045.00:
    INSS=salario_bruto*0.075
elif salario_bruto>=1045.01 and salario_bruto<=2089.60:
    INSS=salario_bruto*0.09
elif salario bruto>=2089,61 and salario_bruto<=3134.40:
    INSS=salario_bruto*0.12
elif salario_bruto>=3134.41 and salario_bruto<=6101.06:
    INSS=salario_bruto*0.14
else:
    INSS=671.12
    
base_de_calculo=salario_bruto-INSS-(numero_dependentes*189.59)

if base_de_calculo<=1903.98:
    IRRF=0
elif base_de_calculo>=1903.99 and base_de_calculo<=2826.65:
    IRRF=(base_de_calculo*0.075)-142.80
elif base_de_calculo>=2826.65 and base_de_calculo<=3751.05:
    IRRF=(base_de_calculo*0.15)-354.80
elif base_de_calculo>=3751.06 and base_de_calculo<=4664.68:
    IRRF=(base_de_calculo*0.225)-636.13
else:
    IRRF=(base_de_calculo*0.275)-869.36