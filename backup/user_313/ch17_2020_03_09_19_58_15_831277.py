def eh_bissexto(a):
    resto = a%4
    resto2 = a%100
    resto3 = a%400

    if(resto == 0):
        print('True')
    
    if(resto2 != 0):
        print('True')
    
    if(resto3 == 0):
        print('True')
    
    else:
        print('False')

print(ano(1))


