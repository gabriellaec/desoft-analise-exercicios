def calcula_fibonacci (n):
    fibo=[]
    n1=1
    n2=1
    fibo.append(n1)
    fibo.append(n2)
    i=0
    while i<(n-2):
        tot=fibo[i]+fibo[i+1]
        fibo.append(tot)
        i+=1
    return fibo
    