ano=2000
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('Bissexto')
else:
    print('Não é bissexto')
    
    
def eh_bissexto(ano):
    a = ano
    if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
        return True
    else:
        return False