def maior_primo_menor_que(n):
    if n== 2:
        return n
    elif n>2 and n<= 10:
        a=[n]
        b= len(a[-1])-1
        while b <=len(a):
            if b%n==1:
                return b
            else:
                a.append(b)