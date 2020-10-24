valor = input(int("Qual o valor da casa a comprar?" ))
    
salario = input(int("Qual o seu salário?"))
    
anos = input(int("Em quantos anos pretende comprar a casa?"))

meses = anos * 12 

prestacao = valor / meses

if prestacao > 0.3*salario:
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado')    