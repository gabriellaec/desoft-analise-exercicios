salario_bruto = int(input("Seu salario bruto: "))
dependentes = int(input("numero de dependentes do usuario: "))

if salario_bruto <= 1045.00:
    INSS = (salario_bruto)*0.075
elif 1045.00 < salario_bruto <= 2089.60:
    INSS = (salario_bruto)*0.09
elif 2089.60 < salario_bruto <= 3134.40:
    INSS = (salario_bruto)*0.12
elif 3134.40 < salario_bruto <= 6101.06:
    INSS = (salario_bruto)*0.14    
elif 6101.06 < salario_bruto:
    INSS = 671,12
    
base_de_calculo = (salario_bruto) - INSS - (dependentes)*189.59    
print(base_de_calculo)  