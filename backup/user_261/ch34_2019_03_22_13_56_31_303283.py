a=float(input("deposito:"))
b=float(input("taxa de juros:"))
mes=1
while mes<=24:
    y=a*(1+b)**mes
    print("{0:.2f}".format (y))
    mes+=1   
        
s=y-a
print("{0:.2f}".format(s))