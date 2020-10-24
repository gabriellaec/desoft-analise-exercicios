a=[]
b=int(input("diga uma numero: "))
while b!=0:
    a.append(b)
    b=int(input("diga uma numero: "))
if b==0:
    print (sum(a))