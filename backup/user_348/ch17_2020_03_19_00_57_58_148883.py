def eh_bissexto (ano):
    if ano == 1:
        print ('True')
    elif ano % 4 == 0 or ano % 100 != 0 :
        print ('True')
    else:
        print ('False')

