c=float(input('qual o valor da casa?'))
s=float(input('quanto ganha?'))
a=int(input('quantos anos demora para pagar?'))
p=c/(a*12)
if p>s*0.3:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')