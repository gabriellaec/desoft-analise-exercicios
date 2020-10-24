s=input('seu salário:')

def calcula_aumento(s):   
    if s>=1250:
        y=s*0.1
        return 'Seu aumento ficou {0} reais'.format(y)
    else:
        y=s*0.15
        return 'Seu aumento ficou{0} reais'.format(y)

print(calcula_aumento(s))        