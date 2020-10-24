sal=int(input('Qual é o seu salário bruto?:'))
dep=int(input('Quantos dependentes?:'))
#calculo da alicota do inss
if sal<=1045.00:
    inss=sal*0.075
elif 1045.00<sal<=2089.60:
    inss=sal*0.09
elif 2089.60<sal<=3134.40:
    inss=sal*0.12
elif 3134.40<sal<=6101.06:
    inss=sal*0.14
else:
    inss=671.12
#base do calculo
base=sal-inss-dep*189.59
#calculo da alicota e deduçao
if base<=1903.98:
    ali=0.0
    ded=0.00
elif 1903.98<base<=2826.65:
    ali=0.075
    ded=142.80
elif 2826.65<base<=3751.05:
    ali=0.15
    ded=354.80
elif 3751.05<base<=4664.68:
    ali=0.225
    ded=636.13
else:
    ali=0.275
    ded=869.36
#calculo do irrf
irrf=base*ali-ded

print(irrf)