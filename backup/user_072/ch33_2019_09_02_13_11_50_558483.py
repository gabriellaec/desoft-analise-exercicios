def soma(a):
    y=1/(2**(a))
    return y

n=0
x=0
while n<99:
   x=x+soma(n)
   n=n+1
print(x)