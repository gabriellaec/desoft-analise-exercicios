n=range(1,1001)
m=0
lenm=0
for i in n:
    I=i
    sc=[i]
    while i!=1:
        if i%2=0:
            i=i/2
        else:
            i=3*i+1
        sc.append(i)
    if len(sc)>lenm
        m=I
        lenm=len(sc)
print(m)