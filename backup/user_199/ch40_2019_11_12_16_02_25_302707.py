def fatorial(n):
    i=1
    f=1
    while i<(n+1):
        f*=i
        i+=1
          
    return f
print(fatorial(4))