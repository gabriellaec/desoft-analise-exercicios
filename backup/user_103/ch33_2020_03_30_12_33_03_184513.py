def primos_entre(a,b):
    p=b-a
    while a%2==0 and a<b:
        a=a+1
        if a%2==0:
            p=p-1
        elif a%2!=0:
            a=a+1
            y=3
            if a%y==0:
                y=y+2
                p=p-1
        return p

            
            