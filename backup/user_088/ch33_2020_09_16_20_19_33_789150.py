def primos_entre(a,b):
    p=2
       
    while(p<=b and p>=a):
        if(p%1==0 and p%p==0):
            return p
            p+=1