valor=float(input('Qual o valor da casa?'))
salario=float(input('Qual seu salário'))
anos=int(input('Quantos anos a pagar?'))
prestacao= valor / (anos*12)
prestacaomax= salario * 0.3
if prestacao > prestacaomax:
    print('Empréstimo não aprovado')
elif prestacao <= prestacaomax:
    print('Empréstimo aprovado')