a=int(input('Salário: '))
def calcula_aumento(a):
    y1=a*1.1
    y2=a*1.15
    if a>1250:
        return 'Aumento de R$ {0:.2f}'.format(y1)
    else:
        return 'Aumento de R$ {0:.2f}'.format(y2)
print(calcula_aumento(a))

    