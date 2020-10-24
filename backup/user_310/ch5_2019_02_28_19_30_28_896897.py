def maior_primo_menor_que(n):
    if n== 2:
        return n
    elif n>2:
        i=2
        while i<= n:
            if n%i==0:
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