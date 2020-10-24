a = float (input('Qual o seu salário bruto? '))
b = int (input('Qual o númro de dependentes? '))

#conta para saber INSS
if a <= 1045:
    INSS = a * 0.075
elif a <= 2089.60:
    INSS = a * 0.09
elif a <= 3134.40:
    INSS = a * 0.12
elif a <= 6101.06:
    INSS = a * 0,1
else:
    INSS = 671.12

#conta para base de calculo
bc = a - INSS - b * 189.59

#conta para IRRF
if bc <= 1903.98:
    IRRF = bc * 0 - 0
elif bc <= 2826.65:
    IRRF = bc * 0.075 -	142.80
elif bc <= 3751.05:
    IRRF = bc * 0.15 - 354.80
elif bc <= 4664.68:
    IRRF = bc * 0.225 - 636.13
else:
    IRRF = bc * 0.275 - 869.36

print ('Seu imposto de renda retido na fonte é: {0}'.format (IRRF))