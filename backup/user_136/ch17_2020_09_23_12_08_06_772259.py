def  eh_bissexto(ano):
    if ano%4==0 and ano%100!=0:
        print('True')
    elif ano%400==0:
        print('True')
    else:
        print('False')