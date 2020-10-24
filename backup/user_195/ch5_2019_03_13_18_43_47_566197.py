def eh_primo(n):
    if n==0 or n==1:
        return False
    elif n==2:
        return True
    else:
        i=1
        p=0
        metade=n/2
        while i<=n:
            if n%2==0:
                p=1
                break
            if n%i==0:
                i+=1
                p+=1
            if i>=metade:
                i=n
                p+=1
                i+=1
            else:
                i+=1
        if p==2:
            return True
        else:
            return False
if eh_primo=True:
	print(n)
elif n<0:
    print ("-1")
else:
    while eh_primo=False:
    	n-=1
    print(n)