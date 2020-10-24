def calcula_pi(n)
a=[]*n
s=0
i=1
while i<n:
    b=6/(i**2)
    s+=b
    i+=1
pi=s**(1/2)