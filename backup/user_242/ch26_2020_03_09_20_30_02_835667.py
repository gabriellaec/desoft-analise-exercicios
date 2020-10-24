v = float (input('Qual o valor da casa?'))
s = float (input('Qual o sálario?'))
a = float (input('Quantidade de anos a pagar?'))

def valor_da_prestacao(v,a):
    p = v/a
    if p > (30/100)* s:
        return 'Empréstimo não aprovado'
    else:
        return 'Empréstimo aprovado'
print ( valor_da_prestacao(v,a))