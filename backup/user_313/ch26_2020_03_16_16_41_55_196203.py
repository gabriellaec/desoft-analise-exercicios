a = float(input('Qual o valor da casa ? ')) 
b = float(input('Qual o seu salario ? '))
c = float(input('Quantos anos para pagar ? '))

d = c*12
e = a/d
f = b*0.3

if e > f :
    print('Empréstimo não aprovado')

if e < f :
    print('Empréstimo aprovado')