vcasa=int(input('digite o valor da casa a comprar: ' ))
salario=int(input('digite o valor do salario: ' ))
qtanos=int(input('digite a quantidade de anos a pagar: ' ))
prestacao=vcasa/(qtanos*12)
if prestacao>0.3*salario:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')