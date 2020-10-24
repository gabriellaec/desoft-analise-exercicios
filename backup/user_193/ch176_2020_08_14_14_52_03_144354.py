def imprime_grade(n):
    c=1
    while c<=n:
        print(n*"+-" + '+')
        print(n*"| " + '|')
        c+=1
    print(n*"+-" + '+')