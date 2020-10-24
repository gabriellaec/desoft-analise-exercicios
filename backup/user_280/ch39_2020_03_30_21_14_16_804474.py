def forma_lista(k):
    n=[]
    b=len(n)
    n[0] = k
    while n[b-1] > 1:
        if n[i]%2 == 0:
            n[i+1] = n[i]/2
        else:
            n[i+1] = 3*n[i] + 1
        i+=1
    return n