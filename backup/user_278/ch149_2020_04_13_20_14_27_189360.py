s_bruto = float(input("Qual o seu salário?: "))

dependentes = int(input("Quantos dependentes?: "))
if s_bruto <=1045.00:
    cont = s_bruto * 0.075
elif 1045.01<= s_bruto <= 2089.60:
    cont = s_bruto * 0.09
elif 2089.61<= s_bruto <=3134.40:
    cont = s_bruto * 0.12	
elif 3134.41<= s_bruto <= 6101.06:
    cont = s_bruto * 0.14
else:
    cont = 671.12

bdc = s_bruto - cont - (dependentes * 189.59)

if bdc <= 1903.98:
    al = 0
    ded = 0
elif 1903.99 <= bdc <= 2826.65:
    al = 0.075
    ded = 142.80
elif 2826.66 <= bdc <= 375105:
    al = 0.15
    ded = 354.80
elif 3751.06 <= bdc <= 4664.68:
    al = 0.225
    ded = 636.13
else:
    al = 0.275
    ded = 869.36

IRRF = (bdc * al) - ded	

print (IRRF)