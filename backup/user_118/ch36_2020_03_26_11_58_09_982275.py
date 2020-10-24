def fatorial (n,i):
    f=n*i
    return f
i=1
f=1
n=4
while i<=n:
    f*=i
    i+=1
print (fatorial(n))