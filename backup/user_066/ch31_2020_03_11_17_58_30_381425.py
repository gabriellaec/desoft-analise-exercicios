def eh_primo(n):
    x = 3
    a = 1 
    if n == 1 or n == 0:
        print('O número {0} não é primo'.format(n))
    elif n == 2:
        print('O número 2 é primo')
    elif n == 3:
        print('O número 3 é primo')
    else:
        if n%2 == 0:
            print('O número {0} não é primo'.format(n))
        else:
            while x<n and a!=0:
                k = n%x
                x += 2    
                if k == 0:
                    a = 0
                    print('O número {0} não é primo'.format(n))
                else:
                    print('O número {0} é primo'.format(n))
                    a = 0
    return True