c = float(input('Qual é o valor da casa?'))
s = float(input('Qual é o seu salário?'))
t = float(input('Vai pagar isso em quantos anos?'))

def f(c, s, t):
    vp = c / (t*12)
    x = s*0.30
    if vp > x:
        return 'Empréstimo não aprovado'
    else:
        return 'Empréstimo aprovado'

print(f(c,s,t))


