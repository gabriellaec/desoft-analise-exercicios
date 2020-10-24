def ehprimo(n):
    if n > 1:
        for i in range(3, n):
            if (n % i) == 0:
                return False
                
            else:
                return True
        if(n==2):
            return True
    else:
        return False
l=[2]
def maior_primo_menor_que(x):
    if(ehprimo(x)==True):
        return x
    elif(ehprimo(x)==False):
        for i in range(2,x+1):
            if(ehprimo(i)==True):
                l.append(i)
        return l[-1]


print(maior_primo_menor_que(11))