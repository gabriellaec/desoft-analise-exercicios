def funcao1(aliquota,salariobruto):
    contribuicao=aliquota*salariobruto
    return contribuicao
    
def funcao2(salariobruto,contribuicao,dependentes,constante):
    base=salariobruto-contribuicao-(dependentes*constante)
    return base

def funcao3(base,aliquota,deducao):
    irrf=base*aliquota-deducao
    return irrf

salariobruto=input('salário?')
dependentes=input('quantos dependentes?')
salariofaixa1=1045
salariofaixa2=2089
salariofaixa3=3134.40
salariofaixa4=6101.06

if salariobruto<=salariofaixa1:
    contribuicao=funcao1(aliquota1,salariobruto)
    deducao=0
    aliquota=0
elif salariobruto<=salariofaixa2:
    contribuicao=funcao1(aliquota2,salariobruto)
    deducao=142.8
    aliquota=0.075
elif salariobruto<=salariofaixa3:
    contribuicao=funcao1(aliquota3,salariobruto)
    deducao=354.8
    aliquota=0.09
elif salariobruto<=salariofaixa4:
    contribuicao=funcao1(aliquota4,salariobruto)
    deducao=636.13
    aliquota=0.12
else:
    contribuicao=funcao1(aliquota5,salariobruto)
    deducao=839.36
    aliquota=0.15

base=funcao2(salariobruto,contribuicao,dependentes,189.59)
irrf=funcao3(base,aliquota,deducao)
print(irrf)