def imprime_grade (n):
    for i in range (n+1):
        if i%2 == 0:
            for i in range (n):
                if i ==0:
                    print('+',end=' ')
                elif i == n-1:
                    print('-',end=' ')
                    print('+')
                else:
                    print('-',end=' ')
                    print('+',end=' ')
        else:
            for i in range (n):
                if i == n-1:
                    print('|')
                else:
                    print('|',end=' ')
