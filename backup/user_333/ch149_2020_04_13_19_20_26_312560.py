s_bruto=float(input('Qual seu salário bruto? '))
n_dependentes=int(input('Qual seu número de dependentes? '))

#Base de cálculo:
if s_bruto<=1045:
    b_calculo=s_bruto-(0.075*s_bruto)-(n_dependentes*189.59)
elif 1045<s_bruto<=2089.6:
    b_calculo=s_bruto-(0.09*s_bruto)-(n_dependentes*189.59)
elif 2089.6<s_bruto<=3134.4:
    b_calculo=s_bruto-(0.12*s_bruto)-(n_dependentes*189.59)
elif 3134.4<s_bruto<=6101.06:
    b_calculo=s_bruto-(0.14*s_bruto)-(n_dependentes*189.59)
else:
    b_calculo=s_bruto-671.12-(n_dependentes*189.59)
    

#IRRF:
if b_calculo<=1903.98:
    irrf=0
elif 1903.98<b_calculo<=2826.65:
    irrf=b_calculo*0.075-142.8
elif 2826.65<b_calculo<=3751.05:
    irrf=b_calculo*0.15-354.8
elif 3751.05<b_calculo<=4664.68:
    irrf=b_calculo*0.225-636.13
else:
    irrf=b_calculo*0.275-869.36
    

print(irrf)