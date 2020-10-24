def lista_primos(n):
    c = 0
    teste = 0
    while c < n:
        if teste == 0 or teste == 1:
            teste += 1
        elif teste == 2 or teste == 3:
            print(teste)
            c += 1
            teste += 1
        elif teste % 2 == 0:
            teste += 1
        else:
            d = 3
            while d < teste:
                if teste % d == 0:
                    teste += 1
                    d = 3
                else:
                    d += 1
            if d == teste:
                print(teste)
                c += 1
                teste += 1
                d = 3