valor_casa=float(input('Qual é o valor da casa'))
salario=float(input('Qual é o valor do salário'))
anos=int(input('Quantos anos se vai pagar'))

prestação=valor_casa/(anos*12)
                 
if prestação<0.3*salario:
    print("Empréstimo aprovado")
    
else:
    print("Empréstimo não aprovado")