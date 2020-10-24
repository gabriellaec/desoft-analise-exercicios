def lista_collatz(x):
    soma=0
    i=x
    while i!=4:
        while i%2==0:
            i=i/2
            soma+=1
        i=3*i + i
        soma+=1
    return soma

d={}
maior=0
for i in range(1,1000):
    d[i]=lista_collatz(i)
    print(i)
print(d)

for n, c in d.items():
    if c>maior:
        maior=c
        num=n
print(num)