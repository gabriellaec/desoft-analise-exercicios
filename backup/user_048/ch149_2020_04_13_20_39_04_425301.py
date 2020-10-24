sb=int(input('Qual o seu salario bruto?'))
dep=int(input('Qual o numero de dependentes?'))
 #taxa de contribuicao para o inss
if sb<=1045:
    i=0.075
elif 1045<sb<=2089.60:
    i=0.09
elif 2089.60<sb<=3134.40:
    i=0.12
elif 3134.40<sb<=6101.06:
    i=0.14
else:
    im=671.12

#contribuicao para o inss
if sb<=6101.06:
    coinss=sb*i
else:
    coinss=im
    
 #A base de cálculo do IRRF simplificado
BC=sb-coinss-(dep*189.59)

#aliquota e deducao
if BC<=1903.98:
    a=0
    d=0
elif 1903.98<BC<=2826.65:
    a=0.075
    d=142.80
elif 2826.65<BC<=3751.05:
    a=0.15
    d=354.80
elif 3751.05<BC<=4664.68:
    a=0.225
    d=636.13
elif 4664.68<BC:
    a=0.275
    d=869.36
    
#IRRF siplificado
irrfs=BC*a-d
print(irffs)