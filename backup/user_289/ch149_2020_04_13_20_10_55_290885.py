salario_bruto = float(input('Qual o salário bruto: '))
n_dependentes = int(input('Qual o número de dependentes: '))

if salario_bruto < 1045:
    contribuicao_INSS = salario_bruto*0.075
elif 1045.01 < salario_bruto < 2089.60: 	
    contribuicao_INSS = salario_bruto*0.09
elif 2089.61 < salario_bruto < 3134.40: 	
    contribuicao_INSS = salario_bruto*0.12
elif 3134.41 < salario_bruto < 6101.06: 	
    contribuicao_INSS = salario_bruto*0.14
else:
    contribuicao_INSS = 671.12

base = salario_bruto - contribuicao_INSS - n_dependentes*189.59
    