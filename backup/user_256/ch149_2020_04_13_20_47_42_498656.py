salario_bruto = float(input("Digite o seu salario bruto: "))
dependentes = int(input("Digite o numero de dependentes: "))

if salario_bruto <= 1045.00:
    bcalc = salario_bruto - salario_bruto*0.075 - dependentes*189.59
elif salario_bruto >= 1045.01 and salario_bruto <= 2089.60:
    bcalc = salario_bruto - salario_bruto*0.09 - dependentes*189.59
elif salario_bruto >= 2089.61 and salario_bruto <= 3134.40:
    bcalc = salario_bruto - salario_bruto*0.12 - dependentes*189.59
elif salario_bruto >= 3134.41 and salario_bruto <= 6101.06:
    bcalc = salario_bruto - salario_bruto**0.14 - dependentes*189.59
else:
    bcalc = salario_bruto - 671.12 - dependentes*189.59

if bcalc <= 1903.98:
    aliquota = 0.0
    deduçao = 0.0
elif bcalc>= 1903.99 and bcalc <= 2826.65:
    aliquota = 0.075
    deduçao = 142.80
elif bcalc >= 2826.66 and bcalc <= 3751.05:
    aliquota= 0.15
    deduçao = 354.80
elif bcalc >= 3751.06 and bcalc <= 4664.68:
    aliquota = 0.225
    deduçao = 636.13
else:
    aliquota = 0.275
    deduçao = 869.36
    
irff = bcalc*aliquota-deduçao    
print(irff)
    
    







