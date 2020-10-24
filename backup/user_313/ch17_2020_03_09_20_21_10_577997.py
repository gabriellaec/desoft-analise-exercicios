def eh_bissexto(ano):

    if(ano%400 == 0):
        print('True')
    if(ano%100 == 0):
        print('False')
    if(ano%4 == 0):
        print('True')
    else:
        return False