def primos_entre(a,b):
    s=[]
    for i in range(a,b+1):
        if i==0 or i==1:
            break
            i+=1
        elif i==2:
            s.append(i)
            i+=1
        else:
            divisores=0
            for divisor in range(1,a):
                if a % divisor ==0:
                    divisores = divisores +1
                if divisores>1:
                    break
                else:
                    s.append(i)
    return(len(s))