valor=float(input('valor do imovel:'))
sal=float(input('salário:'))
anos=float(input('quantidade de anos a pagar:'))
mensal= valor/(anos*12)
porcento= sal*0.3
if mensal > porcento:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')
    