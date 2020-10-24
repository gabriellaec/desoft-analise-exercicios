v=int(input("valor casa:"))
s=int(input("valor Salário:"))
t=int(input("Tempo:"))
if v/t>s*0.3:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')