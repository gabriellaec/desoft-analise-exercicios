def imprime_grade(n):
    for _ in range(n):
        for _ in range(n):
            print('+-', end='')
        print('+')
        for _ in range(n):
            print('| ', end='')
        print('|')
    for _ in range(n):
        print('+-', end='')
    print('+')