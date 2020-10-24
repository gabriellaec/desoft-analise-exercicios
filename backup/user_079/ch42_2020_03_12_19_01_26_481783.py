x=[]
y=True
while y:
    z=str(input('z?:'))
    if z[0]=='a':
        x.append(z)
    if z=='fim':
        y=False
print(x)