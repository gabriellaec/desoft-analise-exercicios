
def eh_bissexto(ano):
    if ano%4==0 and ano%100!=0 and ano!=4:
        return True 
    else:
        return False
    