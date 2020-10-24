p=float(input('Qual é seu salário bruto?'))
p2=int(input('Qual é o seu número de dependentes?'))
if p<=1045.00:
    taxa=0.075
    contribuicao=p*taxa
elif p>=1045.01 and p<=2089.6:
    taxa=0.09
    contribuicao=p*taxa
elif p>=2089.61 and p<=3134.4:
    taxa=0.12
    contribuicao=p*taxa
elif p>=3134.41 and p<=6101.06:
    taxa=0.14
    contribuicao=p*taxa
else:
    taxafixa=671.12
    contribuicao=p-taxafixa

       
base_do_cálculo=p-contribuicao-(p2*189.59)

if base_do_cálculo<=1903.98:
    aliquota=0
    deducao=0
elif base_do_cálculo>=1903.99 and base_do_cálculo<=2826.65:
    aliquota=0.075
    deducao=142.8
elif base_do_cálculo>=28326.66 and base_do_cálculo<=3751.05:
    aliquota=0.15
    deducao=354.8
elif base_do_cálculo>=3751.06 and base_do_cálculo<=4664.68:
    aliquota=22.5
    deducao=636.13
else:
    aliquota=27.5
    deducao=869.36
       
irrf=base_do_cálculo*aliquota-deducao

print(irrf)
       
       