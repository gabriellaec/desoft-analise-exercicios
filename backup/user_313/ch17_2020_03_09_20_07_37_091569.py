def eh_bissexto(a):

    if(a%400 == 0):
        print('True')
    elif(ano%100 == 0):
        print('False')
    elif(ano%4 == 0):
        print('True')
    else:
        return False