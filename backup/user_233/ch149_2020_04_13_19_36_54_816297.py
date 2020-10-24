def obter_contribuicao_inss(salario_bruto):
    
    if salario_bruto <= 1045: return salario_bruto * 0.075
    if salario_bruto <= 2089.60: return salario_bruto * 0.09
    if salario_bruto <= 3134.40: return salario_bruto * 0.12
    if salario_bruto <= 6101.06: return salario_bruto * 0.14
    if salario_bruto > 6101.06: return 671.12

def obter_aliquota_e_deducao_irrf(base_de_calculo):
    
    if base_de_calculo <= 1903.90: return 0, 0
    if base_de_calculo <= 2826.65: return 0.075, 142.80
    if base_de_calculo <= 3751.05: return 0.15, 354.80
    if base_de_calculo <= 4664.86: return 0.225, 636.13
    else: return 0.275, 869.36

def obter_irrf_simplificado(salario_bruto, contribuicao_inss, dependentes):
    
    base_de_calculo = salario_bruto - contribuicao_inss - dependentes * 189.59
    aliquota, deducao = obter_aliquota_e_deducao_irrf(base_de_calculo)
    
    return base_de_calculo * aliquota - deducao
    
salario_bruto = float(input('Salário bruto: '))
dependentes = int(input('Número de dependentes: '))

contribuicao_inss = obter_contribuicao_inss(salario_bruto)
irrf_simplificado = obter_irrf_simplificado(salario_bruto, contribuicao_inss, dependentes)

print(irrf_simplificado)




