def primos_entre(a,b):
    x=0
    while a<=b:
        i=3
        if a==2 or a==3:
            x+=1
            a+=1
        elif a%2==0 or a==1 or a==0:
            a+=1
        else:
            while a%i!=0 and a>i:
                i+=2
            if a==i:
                x+=1
                a+=1
            else:
                a+=1
    return x