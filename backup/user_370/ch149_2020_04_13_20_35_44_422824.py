s_bruto=int(input("Qual seu salario bruto? "))
n_usuarios=int(input("Numero de dependentes do usuario: "))
    
if s_bruto<1045:
    INSS=s_bruto*(7.5/100)
    
elif s_bruto<2089.60:
    INSS=s_bruto*(9/100)
    
elif s_bruto<3134.40:
    INSS=s_bruto*(12/100)
    
elif s_bruto<6101.06:
    INSS=s_bruto*(14/100)

elif s_bruto>6101.06:
    INSS=671.12
    
base= s_bruto - INSS - (n_usuarios*189.59)

if base < 1903.98:
    aliquota=0/100
    deducao=0
    
elif base <2826.65:
    aliquota=7.5/100
    deducao=142.80
    
elif base <3751.05:
    aliquota=15/100
    deducao=354.80
    
elif base <4664.68:
    aliquota=22.5/100
    deducao=636.13
    
elif base >4664.68:
    aliquota=27.5/100
    deducao=869.36
    
IRRF= base * aliquota * deducao 
