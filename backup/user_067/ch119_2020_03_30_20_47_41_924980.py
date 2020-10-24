def calcula_euler(x,n):
    e_x = 0
    for i in range(0, n+1):
        print(fatorial(i))
        e_x = e_x + (x^i)/fatorial(i)

    return e_x
                           
def fatorial(x):                     
    a=x
    if(x==0) or (x==1):
        a = 1
    else:
        while(x>1):
            a = a*(x)
            x = x - 1
    return a