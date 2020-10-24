a=float(input("deposito inicial:"))
b=float(input("taxa de juros:"))
b+=1
i=1
s=0
while i<=24:
    i+=1
    s= a*(b)**i
    print("{0:.2f}".format(s))
print("{0:.2f}".format(s-a))