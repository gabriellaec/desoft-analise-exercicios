a=float(input('valor da casa?'))
b=float(input('salario?'))
c=int(input('quantos anos?'))
d=(a/(c*12))
if d>b*1.3:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')
      
      