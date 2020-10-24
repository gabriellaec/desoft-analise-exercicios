def imprime_primos(n):
    i=2
    c=1
    
    while c<n:
        if teste(i): 
            c+=1 
            print(i)
        i+=1
    while c<=n:
        if teste(i):
            return i
        i+=1
    

    