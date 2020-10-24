salario = float(input("Qual o seu salário bruto bruto? "))
dependentes = int(input('Qual é o numero de dependentes? '))

INSS = 0
if salario <=1045:
    INSS = salario*0.075
elif 1045.01 <= salario <= 2089.6:
    INSS = salario*0.09
elif 2089.61 <= salario <=3134.4:
    INSS = salario*0.12
elif 3134.41 <= salario <= 6101.06:
    INSS = salario*0.14
elif salario > 6101.06:
    INSS = 676.12
print(INSS)
BaseCalc = salario-INSS-(dependentes*189.59)
print(BaseCalc)
IRRF = 0
if BaseCalc <=1903.98:
    IRRF = 0
elif 1903.99 <= BaseCalc <= 2826.65:
    IRRF = (BaseCalc*0.075)-142.8
elif 2826.66 <= BaseCalc <= 3751.05:
    IRRF = (BaseCalc*0.15)-354.8
elif 3751.06 <= BaseCalc <=4664.68:
    IRRF = (BaseCalc*0.225)-636.13
elif BaseCalc > 4664.68:
    IRRF = (BaseCalc*0.275)-869.36
print(IRRF)