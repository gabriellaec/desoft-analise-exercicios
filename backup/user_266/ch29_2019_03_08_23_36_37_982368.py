def calcula_aumento(s):
    a1 = s*1.1
    a2 = s*1.15
    if s > 1250:
        return (int('{0}'.format(a1)))
    else:
        return (int('{0}'.format(a2)))
s = int(input('Qual é o seu salário? '))