def fatorial (n):
    fat=1
    while n>0:
        fat*=n
        n-=1
    return fat
        
def calcula_euler(x,n):
    a=0
    while a<n:
        e= 1*(x**a)/fatorial(a)
        a+=1
    return e
    