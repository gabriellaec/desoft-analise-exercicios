def calcula_euler(x,n):
    print(x,n)
    e_x = 1 + x
    for i in range(0, n):
        print(e_x)
        e_x = e_x + (x^i)/fatorial(x)

    return e_x
                           
def fatorial(x):                     
    a=x
    if(x==0) or (x==1):
        return 1
    else:
        while(x>1):
            a = a*(x-1)
            x = x - 1
    return a