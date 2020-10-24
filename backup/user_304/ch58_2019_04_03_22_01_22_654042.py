def calcula_fibonacci (n):
    fibonacci=[]
    fibonacci.append(1)
    fibonacci.append(1)
    i=2
    while i<=n:
        f=fibonacci[i-1]+fibonacci[i-2]
        fibonacci.append(f)
        i+=1
    return fibonacci[n-1]
