preço=int(input('qual o valor da casa'))
salario=int(input('qual o valor do seu salário'))
tempo=float(input('quanto tempo vai demorar para pagar'))
prestacao=preço/(tempo*12)
if prestacao>salario*0.3:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')