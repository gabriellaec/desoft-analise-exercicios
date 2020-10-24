valor=int(input('Valor da casa:'))
salario=int(input('Salário:'))
anos=int(input('Quantidade de anos a pagar:'))
prestacao=valor/(anos*12)
if prestacao>salario*0.3:
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado')