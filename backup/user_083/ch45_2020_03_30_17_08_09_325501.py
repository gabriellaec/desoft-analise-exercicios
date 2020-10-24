a=[]
while True:
    b=int(input('me diga um numero: '))
    if b<=0:
        break
    a.append(b)
for c in reversed(a):
    print(c)