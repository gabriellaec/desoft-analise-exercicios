def imprime_grade(n):
    for i in range(n):
        for i in range(n):
            print('+', end='')
            print('-', end='')
        print('+')
        for i in range(n):
            print('|', end='')
            print(' ', end='')
        print('|')
    for i in range(n):
        print('+', end='')
        print('-', end='')
    print('+')