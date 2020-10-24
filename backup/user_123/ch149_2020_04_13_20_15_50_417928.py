salbruto = float(input('Escreva seu salário bruto: '))
dependentes = int(input('Escreva o seu número de dependentes: '))
if salbruto <= 1045:
    inss = salbruto*0.075
elif salbruto >= 1045.01 and salbruto <= 2089.6:
    inss = salbruto*0.09
elif salbruto >= 2089.61 and salbruto <= 3134.40:
    inss = salbruto*0.12
elif salbruto >= 3134.42 and salbruto <= 6106.06:
    inss = salbruto*0.14
else:
    inss = 671.12    

base_de_calculo = salbruto - (dependentes*189.59) - inss 

if base_de_calculo <= 1903.98:
    irrf = (base_de_calculo*0)+0
elif base_de_calculo >= 1903.99 and base_de_calculo <= 2826.65:
    irrf = (base_de_calculo*0.075)-142.8
elif base_de_calculo >= 2826.66 and base_de_calculo <= 3751.05:
    irrf = (base_de_calculo*0.15)-354.8
elif base_de_calculo >= 3751.06 and base_de_calculo <= 4664.68:
    irrf = (base_de_calculo*0.225)-636.13
else:
    irrf = (base_de_calculo*0.275)-869.36

print (irrf)