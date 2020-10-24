a= int(input('qual o valor da casa: '))
b= int(input('qual seu salario: '))
c= int(input('quantos anos vai pagar: '))
d= a/(c*12)
e= b*0.3
if d > e:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')