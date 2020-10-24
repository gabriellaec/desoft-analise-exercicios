def calcula_aumento(s):
    if s > 1250:
        return('aumento de {0}'.format(s*0.1))
    elif s <= 1250:
        return('aumento de {0}'.format(s*0.15))
        
print(calcula_aumento(33))