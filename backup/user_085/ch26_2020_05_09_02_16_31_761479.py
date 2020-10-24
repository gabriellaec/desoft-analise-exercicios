c = int(input()) #casa
s = int(input()) #salário
a = int(input()) #anos
m = (c/a)/12
if s *(3/10) < m:
  print('Empréstimo aprovado')
else:
  print('Empréstimo não aprovado')