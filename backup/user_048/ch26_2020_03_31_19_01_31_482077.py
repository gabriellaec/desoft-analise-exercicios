c=int(input("Qual o valor da casa"))
s=int(input("Qaul o salario"))
t=int(input("Quantos anos"))

n=t*12      
p=c/n

if p>0.3*s:
      print('Empréstimo não aprovado')
else:
      print('Empréstimo aprovado')