

def calcula_aumento(s):   
    if s>=1250:
        y=s*0.1
        return 'Seu aumento ficou {0:.2f} reais'.format(y)
    else:
        y=s*0.15
        return 'Seu aumento ficou{0:.2f} reais'.format(y)
s=1200
print(calcula_aumento(s))        