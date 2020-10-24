s=1200

def calcula_aumento(s):   
    if s<=1.250:
        y=s*0.15
        return 'Seu salário com o aumento ficou {0} reais'.format(y)
    else:
        y=s*0.1
        return 'Seu salário com o aumento ficou{0} reais'.format(y)

print(calcula_aumento(s))        