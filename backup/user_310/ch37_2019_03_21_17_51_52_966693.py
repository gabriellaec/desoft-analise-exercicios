def imprime_primos(a):
    lista_primos=[]
    
    n=2
    i=2
    while n<=a:
        if n%i==0:
            n+=1
            i+=1
        else:
            print(n)
            i=2
            n+=1