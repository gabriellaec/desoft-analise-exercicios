s=1000

def calcula_aumento(s):   
    if s<=1.250:
        y=s*0.15+s
        return 'Seu salário com o aumento ficou {0:.2f} reais'.format(y)
    else:
        y=s*0.1+s
        return 'Seu salário com o aumento ficou{0:.2f} reais'.format(y)

print(calcula_aumento(s))        