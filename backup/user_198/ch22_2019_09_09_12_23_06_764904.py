def eh_bissexto(ano):
    if ano%400==0:
        bis=True
    elif ano%100!=0 and ano%4==0: 
        bis=True
    else: bis=False
    return bis
        