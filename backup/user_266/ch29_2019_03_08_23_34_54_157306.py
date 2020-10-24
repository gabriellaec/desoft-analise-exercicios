def calcula_aumento(s):
    if s > 1250:
        a1 = s*1.1
        return (float('{0:.2f}'.format(a1)))
    else:
        a2 = s*1.15
        return (float('{0:.2f}'.format(a2)))
s = float(input('Qual é o seu salário? '))