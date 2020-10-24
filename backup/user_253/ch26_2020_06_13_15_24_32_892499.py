valor = leiaint('quantos cigarros voce fuma por dia?' ))
salario = leiaint('a quantos anos fuma?' ))
anos = leiaint('anos?' )
meses = anos * 12
prestacao = valor / meses  
if prestacao > salario*30/100:
           print('Empréstimo não aprovado')
else:
           print('Empréstimo aprovado')
