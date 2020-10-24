i=0
a=1/(2**i)
while i<99:
    a+=1/(2**(i+1))
    i+=1
print(a)