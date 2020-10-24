v=int(input("qual o valor da casa"))
s=int(input("qual seu salario"))
q=int(input("por wuantos anos"))
p=v/(q*12)
if p>0.3*s:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')
     
      