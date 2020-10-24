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
    elif n>10:
        c=2
        while c<10:
            if n%c==0:
                c+=1
                return n
            else:
                d=[n]
                e= len(d[-1])-1
                f=2
                while e >=10:
                    if e%f==0:
                        return e
                    else:
                        d.append(e)
    else:
        return (-1)