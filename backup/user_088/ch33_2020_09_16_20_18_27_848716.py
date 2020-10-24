def primos_entre(a,b):
    p=1
    if(p==2 and p==3):
        return  p
    while(p<=b and p>=a):
        if(p%1==0 and p%p==0):
            return p
            p+=1