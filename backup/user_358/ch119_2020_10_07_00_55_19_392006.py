contador=0
def calcula_euler (x,n):
    while contador<n:
        contador+=1
        a=contador+1
        e=1+x+(x**(contador+1)/a*(a-contador))
    return e