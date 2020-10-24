salario_bruto=float(input('Qual é o seu salario?')
dependentes=int(input("Quantos dependentes?")
if salario_bruto<=1045:
                base_de_calculo= salario_bruto + salario_bruto*(7,5/100)-dependentes*189,59
elif 1045.01<=salario_bruto<=2089.60:
                base_de_calculo= salario_bruto + salario_bruto*(9/100)-dependentes*189,59
elif 2089.61<=salario_bruto<=3134.40:      
                base_de_calculo= salario_bruto + salario_bruto*(12/100)-dependentes*189,59
elif 3134.41<=salario_bruto<=6101.06:  
                base_de_calculo= salario_bruto + salario_bruto*(14/100)-dependentes*189,59
else:
                base_de_calculo= salario_bruto + 671.12-dependentes*189,59
return base_de_calculo
                 
                 
                 