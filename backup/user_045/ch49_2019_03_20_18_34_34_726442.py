n=[]
n.append(int(input('numeros')))
i=0
while n[i]>0:
    n.append(int(input('numeros')))
    i+=1
n.reverse
print(n)