sal=int(input("quanto você recebe de salário bruto?"))
dependentes=int(input("quantos dependentes você tem?"))
if sal<=1045.00:
    ali= 0.075
if sal>1045.00 and sal<2089.60:
    ali=0.09
if sal>2089.60 and sal<3134.40:
    ali=0.12
if sal<3134.40 and sal<6101.06:
    ali=0.14
def funcao_inss(sal,ali):
    inss=sal*ali
    return inss
if sal<6101.06:
    inss=671.12    
def funcao_bc(sal,inss,dependentes):
    bc=sal-funcao_inss-(dependentes*189.59)
    return bc
if bc<=1903.98:
    aliq=0
    dedu=0      
if bc>1903.98 and bc<2826.65:
    aliq=0.075
    dedu=142.80      
if bc>2826.65 and bc<3751.05:
    aliq=0.15
    dedu=354.80
if bc>3751.05 and bc<4664.68:
    aliq=0.225
    dedu=636.13
if bc>4664.68:
    aliq=0.275
    dedu=869.36
def funcao_irrf(bc,aliq,dedu):
    irrf=funcao_bc*aliq-dedu
    return irrf
   
print (irrf)

