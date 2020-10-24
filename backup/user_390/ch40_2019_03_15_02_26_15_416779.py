n=int(input('valor de n'))
def fatorial(n):    
    i=1
    resultado=1
    while i<=n:
       resultado=resultado* i
       i+=1
    return resultado
print (fatorial(n))