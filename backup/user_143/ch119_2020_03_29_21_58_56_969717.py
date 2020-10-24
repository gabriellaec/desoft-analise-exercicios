def fatorial (n):
    fat=1
    if n==0:
        fat=1
        return fat
    else:
        while n>0:
            fat*=n
            n-=1
        return fat
def calcula_euler(x, n):
    a=0
    e=0
    while a<n:
        e+=(x**a)/fatorial(a)
        a+=1
    return e