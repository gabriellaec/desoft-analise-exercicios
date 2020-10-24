def imprime_tabuada(n):
    c=1
    c2=1
    while c<=n:
        x=c2
        for i in range (n):
            print(x)
            x+=c2
        c+=1
        c2+=1