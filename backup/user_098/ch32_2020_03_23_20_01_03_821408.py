def lista_primos(num):
    if num < 0:
        print("Negativoh")
    else:
        if num >= 1:
            print("2")
            a = 1
            b = 3
            while a<num:
                c=3
                while c<b:
                    if b%c == 0:
                        break
                    c=c+2
                if c == b:
                    print(c)
                    a=a+1
                b=b+2