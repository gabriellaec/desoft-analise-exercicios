x=float(input('Qual é o seu salário?'))
y=int(input('Qual é seu numero de dependentes?'))
if x<=1045:
    aliquota=0.075
    bdc=x-(x*aliquota)-(y*189.59)
elif x>=1045.01 and x<=2089.6:
    aliquota=0.09
    bdc=x-(x*aliquota)-(y*189.59)
elif x>=2089.60 and x<=3134.4:
    aliquota=0.12
    bdc=x-(x*aliquota)-(y*189.59)
elif x>=3134.41 and x<6101.06:
    aliquota=0.14
    bdc=x-(x*aliquota)-(y*189.59)
elif x>=6101.07:
    aliquota=671.12
    bdc=x-aliquota-y*189.59
if bdc<=1903.98:
      deducao=0
      aliquota=0
elif bdc>=1903.99 and bdc<=2826.65:
      deducao=142.8
      aliquota=0.075
elif bdc>=2826.66 and bdc<=3751.05:
      deducao=354.8
      aliquota=0.15
elif bdc>=3751.06 and bdc<=4664.68:
      deducao=636.13
      aliquota=0.225
elif bdc>=4664.69:
      deducao=869.36
      aliquota=0.275
IRRF= bdc*aliquota-deducao

print (IRRF) 