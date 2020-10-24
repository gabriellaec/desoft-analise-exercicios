d=float(input("D"))
a=float(input("a"))
t=float(input("t"))
total=d
i=1
while i <24:
    total+=total*t+a
    print(total-d)

print (total-d)