def imprime_tabuada(n):
    c=1
    c2=1
    while c<=n:
        x=c2
        for i in range (n):
            print(x, end=' ')
            x+=c2
        print("")
        c+=1
        c2+=1