def lista_primos(n):
    contador=1
    num=1
    while contador<n:
        a=3
        if num==0 or num==1:
            num+=1
            continue
        elif num==2 or num==3:
            contador+=1
            print(num)
            num+=1
            continue
        elif num%2==0:
            num+=1
            continue
        else:
            while a<num:
                if num%a==0:
                    resto = num%a
                    break
                else:
                    resto = num%a
                    a=a+2
                if resto ==0:
                    num+=1
                    continue
                else:
                    contador+=1
                    print(num)
                    num+=1
                    continue