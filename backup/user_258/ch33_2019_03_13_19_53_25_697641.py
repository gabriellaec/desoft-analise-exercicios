soma=0
i=1/2**0
n=1
while n<=99:
    soma+=i
    i-=1/2**n
    n+=1
    print(soma)