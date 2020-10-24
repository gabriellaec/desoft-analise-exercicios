x=True
z=0
while x:
    y=int(input("digite um numero: "))
    z+=y
    if y==0:
        print(z)
        x=False
    else:
        continue 