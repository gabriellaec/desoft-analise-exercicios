a=float(input("deposito inicial:"))
b=float(input("taxa de juros de uma poupança :"))
i=1
while i<= 24:
    i+=1
    s= A*(1+b)**i
	print(s)
print(s-a)