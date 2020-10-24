salario_bruto = int(input("Digite aqui seu salário bruto: "))
dependentes = int(input("Digite aqui o número de dependentes da sua renda: "))
inss = 0


if salario_bruto <= 1049:
    inss = 0.075*salario_bruto
elif salario_bruto >= 1049.01 and salario_bruto <= 2089.60:
      inss = 0.09 * salario_bruto
elif salario_bruto >= 2089.61 and salario_bruto <= 3134.40:
    inss = 0.12 * salario_bruto
elif salario_bruto >= 3134.41 and salario_bruto <= 6101.06:
    inss = 0.14 * salario_bruto
else:
    inss = 671.12
   
    
    
base_de_calculo = salario_bruto - inss - dependentes * 189.59
aliquota = 0 
dedução = 0 

if base_de_calculo <= 1903.98: 
    aliquota = aliquota
    dedução = dedução
elif base_de_calculo >= 1903.99 and base_de_calculo <= 2826.65:
    aliquota = 0.075
    dedução = 142.80
elif base_de_calculo >= 2826.66 and base_de_calculo <= 3751.05:
    aliquota = 0.15
    dedução = 354.80
elif base_de_calculo >= 3751.06 and base_de_calculo <= 4664.68:
    aliquota = 0.225
    dedução = 636.13
else: 
    aliquota = 0.275
    dedução = 869.36




IRRF = (base_de_calculo * aliquota) - dedução
