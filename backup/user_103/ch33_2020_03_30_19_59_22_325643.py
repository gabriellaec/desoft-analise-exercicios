def primos_entre(a,b):
    p=b-a
    while a%2==0 and a<=b:
        p=p-1 
        a=a+1
    else:
        y=3
        if a%y==0:
            y=y+2
            p=p-1
        return p

            
            