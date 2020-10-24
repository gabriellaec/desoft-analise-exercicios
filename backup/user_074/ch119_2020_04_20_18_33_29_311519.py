def calcula_euler(x,n):
    i=0
    i+=1
    a=0
    e=0
    while a<n:
        e+= (((x**i)/n*a)**1/x)
        n+=1
        a+=1
        return e