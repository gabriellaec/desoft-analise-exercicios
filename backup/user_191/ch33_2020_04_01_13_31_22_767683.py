a=2
b=3
s=[]
y=[]
i=a
while i<=b:
    if i==0 or i==1:
        y.append(i)
        i+=1
    elif i==2:
        s.append(i)
        i+=1
    else:
        divisores=0
        for divisor in range(1,i):
            if i%divisor == 0:
                divisores = divisores +1
            if divisores>1:
                y.append(i)
                i+=1
            else:
                s.append(i)
                i+=1
print(len(s))