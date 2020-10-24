v=int(input('Qual o valor da casa? '))
s=int(input('Qual seu salario? '))
a=int(input('Quantos anos ira demorar para pagar? '))

if v/(a/12)>((0.3)*s):
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado')