def eh_bissexto(a):

    if(a%400 == 0):
        print('True')
    if(a%100 == 0):
        print('False')
    if(a%4 == 0):
        print('True')
    else:
        return False