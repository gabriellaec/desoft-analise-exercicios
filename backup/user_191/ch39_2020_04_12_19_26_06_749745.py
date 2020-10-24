for n in range(1,1000):
    soma=1
    while n!=1:
        if n%2==0:
            n=n/2
            soma+=1
        else:
            n=3*n+1
            soma+=1
    a=[]
    a.append(soma)
print(index(max(a)))