#comoiniciar um n?
controle=1
n=999
while n<2998:
    if n%2==0:
        n=n/2
        controle+=1
    else:
        n=3*n+1
        controle+=1
n-=1
print(n)