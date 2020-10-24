
def eh_bissexto(ano):
    ano%4==0 = True
    ano/100!==0 = False
    ano%400==0 = True
    if ano%4==0 and ano/100!=0 and ano%400==0:
        return
        