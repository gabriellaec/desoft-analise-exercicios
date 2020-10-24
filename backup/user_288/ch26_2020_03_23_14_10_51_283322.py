valor_casa = int (input ('Qual o valor da casa a comprar? '))
salario = int (input ('Qual seu salario? '))
anos = int (input ('Em quantos anos você quer pagar? '))
            
prestacao = valor_casa / (anos * 12)
if prestacao > 0.3 * salario:
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado')