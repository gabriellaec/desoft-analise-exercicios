x = float(input('Qual o valor da casa?'))
y = float(input('Qual seu salário?'))
z = float(input('Qual a quantidade de anos a pagar?'))

def prestacao(x,y,z):
    n = (x)/(12*z)
    if n > 0.3*y:
        return 'Empréstimo não aprovado'
    else:
        return 'Empréstimo aprovado'
    

