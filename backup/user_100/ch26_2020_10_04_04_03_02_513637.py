c = flout(input('Qual é o valor da casa?'))
s = flout(input('Qual é o seu salário?'))
t = flout(input('Vai pagar isso em quantos anos?'))

def f(c, s, t):
    vp = c / (t*12)
    x = s*0.30
    if vp > x:
        return 'Empréstimo não aprovado'
    else:
        return 'Empréstimo aprovado'

