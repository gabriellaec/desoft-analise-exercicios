import random
n=[]
b=len(n)
n[0] = random.randint(1,1000)
while n[b-1] > 1:
    if n[i]%2 == 0:
        n[i+1] = n[i]/2
        i += 1
    else:
        n[i+1] = 3*n[i] + 1
        i+=1
print(b)