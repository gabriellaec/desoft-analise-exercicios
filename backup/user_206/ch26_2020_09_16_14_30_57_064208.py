casa = int(input('Qual o valor da casa?'))
s = int(input('Qual o seu salário?'))
anos = int(input('Quantos anos para pagar?'))
if casa / anos * 12 <= 0.3 * s:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')