a=[]
for n in range(2,1001):
    soma=1
    while n!=1:
        if n%2==0:
            n=n/2
            soma+=1
        else:
            n=3*n+1
            soma+=1
    a.append(soma)
print(a.index(max(a)))