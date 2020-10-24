a = float (input('Qual o seu salário bruto? '))
b = int (input('Qual o númro de dependentes? '))

#conta para saber INSS
if a <= 1045:
    INSS = a * 0.075
    print (INSS)
elif a >= 1045.01 and a <= 2089.60:
    INSS = a * 0.09
    print (INSS)
elif a >= 2089.61 and a <= 3134.40:
    INSS = a * 0.12
    print (INSS)
elif a >= 3134.41 and a <= 6101.06:
    INSS = a * 0.14
    print (INSS)
else:
    INSS = 671.12
    print (INSS)

#conta para base de calculo
bc = a - INSS - (b * 189.59)
print (bc)

#conta para IRRF
if bc <= 1903.98:
    IRRF = bc * 0 - 0
    print(IRRF)
elif bc >= 1903.99 and bc <= 2826.65:
    IRRF = bc * 0.075 -	142.80
    print(IRRF)
elif bc >= 2826.66 and bc <= 3751.05:
    IRRF = bc * 0.15 - 354.80	
    print(IRRF)
elif bc >= 3751.06 and bc <= 4664.68:
    IRRF = bc * 0.225 - 636.13
    print(IRRF)
else:
    IRRF = bc * 0.275 - 869.36
    print(IRRF)

print ('Seu imposto de renda retido na fonte é: {0}'.format (IRRF))