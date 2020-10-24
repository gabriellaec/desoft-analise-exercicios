def maior_primo_menor_que(n):
    if n== 2:
        return n
    elif n>2 and n<= 10:
        i=1
        while i<= n:
            if n%2==1:
                i+=1
                return n
            else:
                a=[n]
                b= len(a[-1])-1
                while b >=3:
                    if b%n==1:
                        return b
                    else:
                        a.append(b)
    else:
        return (-1)