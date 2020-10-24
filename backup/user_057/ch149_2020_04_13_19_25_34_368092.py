salario_bruto = input("Seu salario bruto: ")
dependentes = input("numero de dependentes do usuario: ")

if salario_bruto <= 1045.00:
    INSS = (salrio_bruto)*0.075
elif 1045.00 < salario_bruto <= 2089.60:
    INSS = (salrio_bruto)*0.09
elif 2089.60 < salario_bruto <= 3134.40:
    INSS = (salrio_bruto)*0.12
elif 3134.40 < salario_bruto <= 6101.06:
    INSS = (salrio_bruto)*0.14    
elif 6101.06 < salario_bruto:
    INSS = 671,12
    
base_de_calculo = (salario_bruto) - INSS - (dependentes)*189.59    
  