def calcula_imposto_de_renda(x,y):
    x=int(input('Qual o seu salário bruto? '))
    y=int(input('Quantos dependentes você possui? '))
    while x>0:
        if x<=1045:
            aliquota=0.075
            contribuicao=x*aliquota
            break
        elif x>1045 and x<=2089.60:
            aliquota=0.09
            contribuicao=x*aliquota
            break
        elif x>2089.60 and x<=3134.40:
            aliquota=0.12
            contribuicao=x*aliquota
            break
        elif x>3134.40 and x<=6101.06:
            aliquota=0.14
            contribuicao=x*aliquota
            break
        else:
            aliquota=671.12
            contribuicao=aliquota
            break
    base_de_calculo=x-contribuicao-(y*189,59)
    while base_de_calculo>0:
        if base_de_calculo<=1903.98:
            aliquota2=0
            deducão=0
            break
        elif base_de_calculo>1903.98 and base_de_calculo<=2826.65:
            aliquota2=0.075
            deducao=142.80
            break
        elif base_de_calculo>2826.65 and base_de_calculo<=3751.05:
            aliquota2=0.15
            deducao=354.80
            break
        elif base_de_calculo>3751.05 and base_de_calculo<=4664.68:
            aliquota2=0.225
            deducao=636.13
            break
        else:
            aliquota2=0.275
            deducao=869.36
            break
    irrf=(base_de_calculo*aliquota2)-deducao
    return irrf
print(calcula_imposto_de_renda(x,y))
    