def prestacao(m):
    n = (x)/(12*z)
    if n > 0.3*y:
        return 'Empréstimo não aprovado'
    else:
        return 'Empréstimo aprovado'
    
x = int(input('Qual o valor da casa?'))
y = int(input('Qual seu salário?'))
z = int(input('Qual a quantidade de anos a pagar?'))
