def emprestimo(a,b,c):
    m = c*12
    pm = a/m
    x = b*0.3
    if pm > x:
        return ('Empréstimo não aprovado')
    else: 
        return ('Empréstimo aprovado')

v = float(input('Valor da casa: '))
s = float(input('Qual seu salario? '))
t = int(input('Em quantos anos pretende pagar? '))