a=float(input("deposito inicial:"))
b=float(input("taxa de juros de uma poupança :"))
i=1
s=0
while i<= 24:
    i+=1
    s= a*(1+b/100)**i
	print(s)
print{0:.2f}.format(s-a)