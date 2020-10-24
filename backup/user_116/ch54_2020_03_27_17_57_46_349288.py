def calcula_fibonacci(n):
    fib=[1,1]
    i=1
    o=0
    if n==1:
        del fib[1]
        return fib

    else:
        while o<n-2:
            if n!=1:
                fib.append(fib[i]+fib[i-1])
                i+=1
                o+=1       
        return fib