n = 0
while n <1000 and n>=0:
    n+=1
    l = []
    if n % 2 ==0:
    	l.append(n/2)
        n-=1
        if n == 0:
            break
	elif n % 2 !=0:
    	l.append((3*n)+1)
    	n-=1
        if n == 0:
            break
print(n)