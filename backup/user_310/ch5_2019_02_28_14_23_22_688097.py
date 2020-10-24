def maior_primo_menor_que(n):
    if n== 2:
        return n, True
    elif n>2:
        i=1
        while i<= n:
            if n%2==1:
                i+=1
                return n, True
            else:
                a=[n]
                b= len(a[-1])-1
                while b >=3:
                    if b%n==1:
                        return b, False
                    else:
                        a.append(b)
    else:
        return (-1)