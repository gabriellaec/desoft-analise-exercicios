def eh_primo(n):
    if n==0 or n==1:
        print ("Não é primo não")
    else:
        i=1
        p=0
        metade=n/2
        while i<=n:
            if n%i==0:
                i+=1
                p+=1
            if i>=metade:
                i=n
                p+=1
                i+=1
            else:
                i+=1
        if p==2:
            print ("É primo")
        else:
            print("Isso não é primo não")
                
print(eh_primo(1))    