sb = float(input("Qual é o salário bruto? "))
nd = int(input("Qual é o numero de dependentes? "))

if sb <= 1045.00:
    inss =  sb *0.075

elif sb >1045.00 and sb <= 2089.60:
    inss =  sb *0.09

elif sb > 2089.60 and sb <= 3134.40:
    inss = sb *0.12

elif sb > 3134.40 and sb <= 6101.06:
    inss = sb *0.14

else:
    inss = 671.12
    
base = sb - inss - nd * 189.59

if base  <= 1903.98:
    ali2 = 0
    deducao = 0

elif base  >1903.98 and base <= 2826.65:
    ali2 = 0.075
    deducao = 142.80

elif base > 2826.65 and base <= 3751.05:
    ali2 = 0.15
    deducao =354.80
    
elif base > 3751.05 and base <= 4664.68:
    ali2 = 0.225
    deducao =636.13
    
else:
    ali2 = 0.275
    deducao =869.36
    
IRRF = (base * ali2) - deducao

print("o IRRF simplificado é {}".format(IRRF))