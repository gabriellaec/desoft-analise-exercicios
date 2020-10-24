def calcula_euler(x,n):
    i=0
    i+=1
    a=1
    e=0
    while a<n:
        e+= (((x**i)/((a+n)*a))**1/x)
        n+=1
        a+=1
        print(x)
        print(n)
        print (e)
        return e