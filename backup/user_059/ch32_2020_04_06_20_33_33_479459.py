def lista_primos(n):
    l = []*n
    i = 0
    while i<n:
        if i<2:
            pass
        elif i==2:
            l.append(i)
        else:
            if i%2==0:
                pass
            else:
                j= 3
                while j<n:
                    if i%j==0:
                        break
                    j+=1
                if i==j:
                    l.append(i)
                else:
                    pass
        i+=1
    