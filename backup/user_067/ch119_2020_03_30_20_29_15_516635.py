def calcula_euler(x,n):
    e_x = 1 + x
    for i in range(1, n, 1):
        print(e_x)
        e_x = e_x + (x^2)/fatorial(x)

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