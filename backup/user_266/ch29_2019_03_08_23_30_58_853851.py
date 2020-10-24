s = float(input('Qual é o seu salário? '))
def calcula_aumento(s):
    if s > 1250:
        a1 = s*1.1
        return 'Seu novo salário é: R${0:.2f}'.format(a1)
    else:
        a2 = s*1.15
        return 'Seu novo salário é: R${0:.2f}'.format(a2)
print(calcula_aumento(s))