a=int(input("Qual é o valor da casa?"))
b=int(input("Qual é o salário?"))
c=int(input("Em quantos anos vc quer pagar?"))
if (a/(c*12))>0.3*b:
    print('Empréstimo não aprovado')
elif (a/(c*12))<0.3*b:
    print('Empréstimo aprovado')

