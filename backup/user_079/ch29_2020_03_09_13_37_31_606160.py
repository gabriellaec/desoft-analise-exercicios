x=int(input('deposito inicial?:'))
y=int(input('taxa?:'))
z=(((y/100)+1))
n=1
while n <25:
    zek=x*(z**n)
    print(zek)
    n+=1
print(zek)

