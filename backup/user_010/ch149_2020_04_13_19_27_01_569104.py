bruto=float(input("Qual o seu salário bruto?   "))
dependentes=int(input("Quantos são os dependentes do usuário?   "))

def inss (bruto):
    if bruto<=1045:
        contribuicao=bruto*0.075
    elif bruto>1045 and bruto<=2089.6:
        contribuicao=bruto*0.09
    elif bruto>2089.6 and bruto<=3134.4:
        contribuicao=bruto*0.12
    elif bruto>3134.4 and bruto <=6101.06:
        contribuicao=bruto*0.14
    elif bruto>6101.06:
        contribuicao=671.12
    return contribuicao

imposto=inss(bruto)

def base_calculo (bruto, imposto, dependentes):
    y=bruto-imposto-dependentes*189.59
    return y

base=base_calculo(bruto,imposto, dependentes)

def irrf (base):
    if base<=1903.98:
        aliquota=0
        deducao=0
    elif base>1903.98 and base<=2826.65:
        aliquota=0.075
        deducao=142.8
    elif base>2826.65 and base<=3751.05:
        aliquota=0.15
        deducao=354.8
    elif base>3751.05 and base<=4664.68:
        aliquota=0.225
        deducao=636.13
    elif base>4664.68:
        aliquota=0.275
        deducao=869.36
    y=base*aliquota-deducao
    return y
    
resultado=(irrf(base))


print (resultado)