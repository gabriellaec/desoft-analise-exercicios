def calcula_fibonacci(n):
    ls=[1,1]
    i=1
    if n==1:
        ls=[1]
    elif n==2:
        ls=[1,1]
    else:
        while len(ls)!=n:
            ls.append(ls[i]+ls[i-1])
            i+=1
    return ls
        
        