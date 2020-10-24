valor=float(input('Digite o valor da casa:'))
salário=float(input('Digite o salário:'))
anos=float(input('Quantos anos para pagar:'))
meses = anos * 12
prestacao = valor / meses
if prestacao > salário * 0.3:
    print('Empréstimo não aprovado')
else:
    print('Valor da prestação: R$ %7.2f Empréstimo aprovado' % prestacao)