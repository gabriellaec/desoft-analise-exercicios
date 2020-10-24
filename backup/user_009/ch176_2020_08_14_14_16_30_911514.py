def imprime_grade(n):
    for i in range(n):
        a = '+-'
        print(a*n,end='')
        print('+')
        b =  '| '
        print(b*n,end='')
        print('|')

    print('+-'*n,end='')
    print('+')