v=int(input('digite o valor da casa:'))
s=int(input('digite o seu salário:'))
a=int(input('digite a quantidade de anos a pagar:'))

def f(v,s,a):
    prestacao=v/a*12
  
    if prestacao>s:
        return "Empréstimo não aprovado"
    else:
        return "Empréstimo aprovado"
    
print(f(v,s,a))
    