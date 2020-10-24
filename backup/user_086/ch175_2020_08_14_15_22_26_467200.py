def imprime_tabuada(n):
    i=1
    x=1
    while x<=n:
        i=1
        while i<=n:
            numero=i*x
            print(numero,end=" ")
            i+=1
        print(" ")
        x+=1