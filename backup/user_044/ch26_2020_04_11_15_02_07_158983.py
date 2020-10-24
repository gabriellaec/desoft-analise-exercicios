valor = float(input("Qual o valor da casa? "))
sal = float(input("Qual é o seu salário? "))
anos=float(input("Quantidade de anos: "))
prest=valor/(anos*12)
if prest>0.3*sal:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')
    
    