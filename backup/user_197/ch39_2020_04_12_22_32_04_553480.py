n = 999
sequencias=[]
while n>1:
    i=n
    sequencia_collatz=[i]
    while i>1:
        if i%2==0:
            i=(i/2)
            sequencia_collatz.append(i)
        else:
            i=((i*3)+1)
            sequencia_collatz.append(i)
    sequencias.append(sequencia_collatz)
    n-=1
x=0