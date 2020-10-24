valor=float(input('Qual o valor da casa? '))
salario=float(input('Qual o valor do salario? ')) 
anos=float(input('Quantos anos? '))
meses=anos*12
prestacao=valor/meses
if prestacao>0.3*salario:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado') 