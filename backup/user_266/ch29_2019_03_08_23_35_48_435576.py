def calcula_aumento(s):
    a1 = s*1.1
    a2 = s*1.15
    if s > 1250:
        return (float('{0:.2f}'.format(a1)))
    else:
        return (float('{0:.2f}'.format(a2)))
s = float(input('Qual é o seu salário? '))