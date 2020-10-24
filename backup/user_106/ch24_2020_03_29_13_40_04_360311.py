def calcula_aumento(s):
    if s>1250:
        x=s*1.100
        return x
    else:
        x=s*1.150
        return x

    
def eh_bissexto(ano):
    a = ano
    if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
        return True
    else:
        return False