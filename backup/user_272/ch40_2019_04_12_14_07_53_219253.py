n=int(input('numero'))
x=1
y=1
def fatorial(n):
	while y<=n:
        x=x*y
        y+=1        
    return x
print (x)