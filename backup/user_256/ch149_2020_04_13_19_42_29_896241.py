salario_bruto = float(input("Digite o seu salario bruto: "))
dependentes = int(input("Digite o numero de dependentes: "))
#contribuição INSS
if salario_bruto <= 1045:
    inss = 0.075*salario_bruto
elif salario_bruto > 1045 and salario_bruto <= 2089.60:
    inss = 0.09*salario_bruto
elif salario_bruto > 2089.60 and salario_bruto <= 3134.40:
    inss = 0.12*salario_bruto
elif salario_bruto > 3134.40 and salario_bruto <= 6101.06:
    inss = 0.14*salario_bruto
else:
    inss = salario_bruto + 671.12

#Base de calculo

base_de_calculo = salario_bruto - inss - (dependentes*189.59)

#irff

if base_de_calculo <= 1903.98:
    aliquota = 0.0
    deduçao = 0.0
elif base_de_calculo > 1903.98 and base_de_calculo <= 2826.65:
    aliquota = 0.075
    deduçao = 142.80
elif base_de_calculo > 2826.65 and base_de_calculo <= 3751.05:
    aliquota= 0.15
    deduçao = 354.80
elif base_de_calculo > 3751.05 and base_de_calculo <= 4664.68:
    aliquota = 0.225
    deduçao = 636.13
else:
    aliquota = 0.275
    deduçao = 869.36
    
irff = base_de_calculo*(aliquota)-deduçao    
print(irff)
    
    







