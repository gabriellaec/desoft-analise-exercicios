c=int(input('qual o valor da casa?'))
s=int(input('qual o seu salario?'))
a=int(input('em quantos anos vai pagar?'))
pm=c/(a*12)
x= s*0.3
if pm<=x:
    print('Empréstimo aprovado')
else: 
    print('Empréstimo não aprovado')
    